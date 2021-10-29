#Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
import time
def Calculate(sec):
    #converting seconds to HH:MM:SS
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

#start of the timer
input("Press Enter to start")
start_time = time.time() #get current system Time
print(start_time)
#End of the timer
input("Press Enter to stop")
end_time = time.time()
print(end_time)
time = end_time - start_time
#calling method
Calculate(time)

