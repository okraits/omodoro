# README for omodoro

## Contents:

1. Overview
2. License
3. Feedback, questions and contributions
4. Requirements
5. Usage
6. Customization
7. Todo list

### 1. Overview

omodoro is, as the name suggests, a tool for using the pomodoro technique.

Currently it provides the following features:

- display periodic reminders for pomodori and breaks
- option to pause and continue the cycle
- option to abort the current pomodori or break and start the next one
- commandline argument for user-specific pomodoro cycle
- _/home/$USER/.omodoro.conf_ configuration file for user-specific pomodoro cycle

### 2. License

This software is released under the terms of the
GNU General Public License v2:

[http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt](http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt)

### 3. Feedback, questions and contributions

There is a git repository available at github:

[https://github.com/okraits/omodoro](https://github.com/okraits/omodoro)

This software was initiated by Oliver Kraitschy (http://okraits.de).
Please feel free to send him feedback and questions regarding
bugreports, feature requests, improvements, etc. via github or mail at
[okraits[at]arcor[dot]de](mailto:okraits@arcor.de).

### 4. Requirements

omodoro has the following requirements:

- Python 2 or 3
- libnotify

### 5. Usage

Run the script with python:

`python omodoro`

When omodoro is running, you can type:

- __p__ to pause the current pomodoro cycle
- __c__ to continue the current pomodoro cycle - the end time will be adjusted
- __n__ to abort the current pomodori or break and start the next one
- __q__ to quit omodoro

### 6. Customization

You can adjust the pomodoro cycle to your needs by

1. editing the variables in the __SETTINGS__ section of the omodoro script

2. copying the file _omodoro.conf.sample_ as _.omodoro.conf_ into your home
directory and modifying it

3. adding a commandline argument by running omodoro like this:

`python omodoro P-L-S-B`

with

	P	number of pomodori to do in a cycle
	L	length of one pomodori in minutes
	S	length of a short break in minutes
	B	length of a long break in minutes

Example with the default values:

`python omodoro 4-25-5-15`

### 7. Todo list

These are things which are planned to be done, at some point
in the future.

- require acknowledgement for next pomodoro/break
- gtk GUI
