# Alarm clock made using Python
import time
import datetime
import os

# Entry message
print('Simple alarm clock !')

# User input
alarm_time = int(input('Enter time : (HH:MM:SS)')) # hour:minute:second

# Extract hour, minute, second
alarm_hour = int(alarm_time[0:2])
alarm_minute = int(alarm_time[3:5])
alarm_second = int(alarm_time[6:8])

# Display 
print('Alarm set for :',alarm_time)

# main logic
while True:
    now = datetime.datetime.now() # current time

    if(now.hour == alarm_hour and
       now.minute ==  alarm_minute and
       now.second == alarm_second):
        