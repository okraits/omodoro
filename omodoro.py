#!/usr/bin/python

# pomodoro script by Oliver Kraitschy
# http://okraits.de okraits@arcor.de
# https://github.com/okraits/omodoro
#
# TODO
# -read length of pomodori and breaks from config file
# -add possibilty to pause the process
# -require acknowledgement for next pomodoro/break
# -gtk GUI

from os import system
from datetime import datetime, timedelta
from time import sleep
from threading import Thread

# SETTINGS
# adjust the pomodoro cycle to your needs
num_pomodori = 4 # number of pomodori to do in a cycle
length_pomodori = 25 # length of one pomodori in minutes
length_short_break = 5 # length of a short break in minutes
length_long_break = 15 # length of a long break in minutes


# global variables
class States:
    Pomodori, ShortBreak, LongBreak = range(3)
cnt_pomodori = num_pomodori # pomodori left in the current cycle
cnt_short_breaks = num_pomodori - 1 # short breaks left in the current cycle
end_time = None # end time of the current state
state = States.Pomodori
command = "" # input string

def changeState(newState, length):
    global end_time, state
    title = ""
    description = ""
    if newState == States.Pomodori:
        title = "Next Pomodori"
        description = "Please start with the next Pomodori!\n\nEnd Time:"
    elif newState == States.ShortBreak:
        title = "Short Break"
        description = "Please take a short break!\n\nEnd Time:"
    elif newState == States.LongBreak:
        title = "Long Break"
        description = "Please take a long break!\n\nEnd Time:"
    else:
        # Something went wrong - exit
        exit(1)
    end_time = datetime.now() + timedelta(minutes=length)
    system("notify-send -u critical '%s' '%s %s'" % (title, description, end_time.strftime("%H:%M")))
    state = newState

class PomodoroThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global cnt_pomodori, cnt_short_breaks, state

        while command != "q":
            if state == States.Pomodori:
                # pomodori is not over
                if end_time > datetime.now():
                    pass
                else:
                    # decrease number of pomodori for the current cycle
                    cnt_pomodori -= 1
                    if length_short_break > 0 and cnt_short_breaks > 0:
                        # length of short breaks > 0 and short breaks left -> start short break
                        changeState(States.ShortBreak, length_short_break)
                    elif length_short_break == 0 and cnt_pomodori != 0:
                        # no short breaks -> start next pomodori
                        changeState(States.Pomodori, length_pomodori)
                    elif cnt_pomodori == 0:
                        # last pomodori over -> start long break
                        changeState(States.LongBreak, length_long_break)
                    else:
                        # Something went wrong - exit
                        print("Error - aborting.")
                        exit(1)
            elif state == States.ShortBreak:
                # short break is not over
                if end_time > datetime.now():
                    pass
                else:
                    # decrease number of short breaks for the current cycle
                    cnt_short_breaks -= 1
                    # start next pomodori
                    changeState(States.Pomodori, length_pomodori)
                pass
            elif state == States.LongBreak:
                # long break is not over
                if end_time > datetime.now():
                    pass
                else:
                    # re-init variables, start next cycle
                    cnt_pomodori = num_pomodori
                    cnt_short_breaks = num_pomodori - 1
                    changeState(States.Pomodori, length_pomodori)
            else:
                # Something went wrong - exit
                print("Error - aborting.")
                exit(1)
            sleep(30)
        print("Shutdown finished.")
        

if __name__ == "__main__":

    # start first pomodori
    changeState(States.Pomodori, length_pomodori)
    pomodorothread = PomodoroThread()
    pomodorothread.start()
    while True:
        command = input("> ")
        if command == "q":
            print("omodoro is shutting down, please wait some seconds.")
            exit(0)
