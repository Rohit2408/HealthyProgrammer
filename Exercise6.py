import datetime
import time
import pygame
from pygame import mixer

current_time = time.strftime("%H:%M:%S")
start_time = '9:00:00'
end_time = '17:00:00'
report_file = "Health Report" + str(datetime.datetime.now().date()) + time.strftime("%H:%M:%S").replace(":","-") + ".txt"

water_limit = 3500
glass_size = 200
no_of_glass = round(water_limit / glass_size)
total_time = 8*60*60
water_interval = total_time/no_of_glass
water_mp3 = "water.mp3"

eye_exercise = 45*60
eye_mp3 = "eye.mp3"

physical_exercise = 45*60
physical_mp3 = "physical.mp3"

def water_reminder(glass):
    i = ""
    while (i!="Y"):
        play_music(water_mp3)
        print("\n", end = " ")
        i = input("Did you drink water? If yes press Y: ").lower()
        if i=="Y":
            f = open(report_file, "a")
            f.write("[" + str(datetime.datetime.now()) + "] :" + "Water " + str(glass_size) + "ml \n")
            f.close()
            print("Thank You!!")
            mixer.music.stop()
            time.sleep(water_interval)
            break

def eye_reminder():
    i = ""
    while (i!="done"):
        play_music(eye_mp3)
        print("\n", end = " ")
        i = input("Did you do your eye exercise? If yes type done: ").lower()
        if i=="done":
            f = open(report_file, "a")
            f.write("[" + str(datetime.datetime.now()) + "] :" + "Eye Exercise" + "\n")
            f.close()
            print("Thank You!!")
            mixer.music.stop()
            time.sleep(eye_exercise)
            break

def physical_reminder():
    i = ""
    while (i!="done"):
        play_music(physical_mp3)
        print("\n", end = " ")
        i = input("Did you do your physical exercise? If yes type done: ").lower()
        if i=="done":
            f = open(report_file, "a")
            f.write("[" + str(datetime.datetime.now()) + "] :" + "Physical Esercise" + "\n")
            f.close()
            print("Thank You!!")
            mixer.music.stop()
            time.sleep(physical_exercise)
            break
interval = 0
glass = 0
while(current_time<=end_time):
    if (current_time >= start_time and current_time <= end_time):
        if glass == no_of_glass:
            pass
        else:
            water_reminder(glass)
            glass+=1
        eye_reminder()
        physical_reminder()
        current_time = time.strftime("%H:%M:%S")