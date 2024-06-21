import datetime
from playsound import playsound
alarmHour = int(input("HH: "))
alarmMin = int(input("MM: "))
alarmAm = input("am/pm: ")

if alarmAm=="pm":
    alarmHour+=12
    
while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("ALARM IS ON.... ⏰⏰⏰")
        playsound("your_music.mp3")
        break
