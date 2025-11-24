 Python Console Alarm Clock

Overview of the Project

This project implements a simple, console-based digital alarm clock using Python. Its primary function is to continuously monitor the system clock in real-time and trigger an auditory alert (an MP3 file) when the current time matches a specific time input by the user. The application demonstrates core programming concepts such as time manipulation, external library integration, and basic control flow logic.

Features

Real-Time Clock Display: Prints the current time every second to the console, providing continuous feedback to the user.

Time-Based Trigger: Accurately compares the system time (HH:MM:SS format) against the user-defined alarm time.

Auditory Alert: Uses the pygame library to play a specified MP3 file when the alarm time is reached.

Controlled Playback: Ensures the program remains active until the entire alarm sound file has finished playing.

Self-Termination: Automatically exits the monitoring loop once the alarm has been successfully triggered and played.

Technologies/Tools Used

Tool/Library

Purpose

Python 3.x

Core programming language.

datetime

Handling system time and formatting time strings.

time

Controlling loop delay (time.sleep) for resource efficiency.

pygame

Essential library for audio playback (pygame.mixer).

Steps to Install & Run the Project

Prerequisites

You must have Python 3 installed and the pygame library installed.

Install pygame:

pip install pygame


Alarm Sound File: Ensure you have an audio file named sound.mp3 (or change the sound_file variable in alarm.py) located in the same directory as the alarm.py script.

Running the Program

Save the Code: Save the provided Python code as alarm.py.

Execute: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

python alarm.py


Set Alarm: The program will prompt you to enter the alarm time:

enter the time: HH:MM:SS


Enter the time using two-digit hour, minute, and second format (e.g., 07:30:00 or 14:05:00).

Instructions for Testing

To confirm the alarm functions correctly, follow these testing steps:

Preparation: Note the current time displayed on your computer.

Test Case 1 (Standard Trigger):

Input an alarm time that is 30 to 60 seconds ahead of the current time (e.g., if it is 10:15:05, set the alarm for 10:16:00).

Expected Result: The console log should tick up to the target time. When the time matches, the alarm message should print, and the sound should play immediately. The program should then terminate.

Test Case 2 (Immediate Trigger Check):

Restart the program.

Input an alarm time that is only 5 seconds ahead of the current time.

Expected Result: The quick trigger verifies the low latency of the time-checking loop.

Audio Validation (TC-04):

Ensure the sound.mp3 file is long enough to verify the loop.

Observation: Confirm that the program stays running (the console doesn't return control) for the full duration of the song playback before closing, validating the while pygame.mixer.music.get_busy(): functionality.
