import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Take a break.")

# 设置专注时间为25分钟
focus_timer(25)
