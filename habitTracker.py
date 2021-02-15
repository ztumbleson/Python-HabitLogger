#**********************************
#
# File - habitTracker.py
#
# Created - 02/15/2021
#
# Author - Zachary Tumbleson
#
#**********************************

from datetime import date

#Intro text
print("Welcome to the Habit Tracker!\n************************************\n")
print("\nTo change the habits that are prompted for here, simply change the code in habitTracker.py")
print("Now then, let's get the raw data collection out of the way.\n")

#sleep tracking
bedTime = input("What time did you go to bed last night?: ")
wakeTime = input("What time did you wake up this morning?: ")
hoursSlept = input("I don't feel like doing the math, how many hours is that?: ")

#fitness tracking
weight = input("What was your weight this morning?: ")
workout = input("What workout did you do this morning?: ")

#misc
meditate = input("Did you meditate?: ")

print("Thanks, I'll get that right out to you, one moment...")

today = date.today()
today_string = '{:%m_%d_%y}'.format(today)
newFile = open("Habits_" + today_string + ".txt", "w")

newFile.write("Tracking Data for " + today_string + "\n************************************")

#write sleep data
newFile.write("\n\nSleep: \n************************************")
newFile.write("\nBed Time: " + bedTime)
newFile.write("\nWake Time: " + wakeTime)
newFile.write("\nHours Slept: " + hoursSlept)

#Write fitness data
newFile.write("\n\nFitness: \n************************************")
newFile.write("\nWeight: " + weight)
newFile.write("\nWorkout: " + workout)

#misc
newFile.write("\n\nMiscellaneous Trackers: \n************************************")
newFile.write("\nMeditate: " + meditate)

newFile.close()