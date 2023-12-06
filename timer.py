import time
seconds=input("Enter The Time In Number Of Seconds")
def countDownTimer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer)
        time.sleep(1)
        seconds-=1
countDownTimer(int(seconds))    