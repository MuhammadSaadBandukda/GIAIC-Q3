import time

def countdown(t):
    while t:
        sec = t%60
        minutes = t//60
        print(f"{str(minutes).zfill(2)}:{str(sec).zfill(2)}",end="\r")
        time.sleep(1)
        t-=1
    print("00:00")
    print("The countdown finished")
countdown(10)