#countdown timer
print("_______Welcome to Time Countdown Clock_______")
print()
import time
hour = int(input("Enter time is Hours: "))
min = int(input("Enter time is Minutes: "))
sec = int(input("Enter time is Second: "))

my_time = (hour*3600)+(min*60)+(sec)

for i in range(my_time,0,-1):
    second = i % 60
    minutes = int(i/60)%60
    hours = int(i/3600)
    print(f'{hours:02}:{minutes:02}:{second:02}')
    time.sleep(1)
print("00:00:00")
time.sleep(1)
print("Time Countdown is Finished")