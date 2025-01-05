import datetime
import time
import random
import os
import webbrowser

if not os.path.isfile("link.txt"):
    print("creating 'link.txt'...")
    with open("link.txt", "w") as alarm_file:
        alarm_file.write("https://www.instagram.com/ryxagnrl/")

def check_alarm_input(alarm_time):
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
        
