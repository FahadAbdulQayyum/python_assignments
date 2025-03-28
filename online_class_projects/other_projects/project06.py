## Project 6: Countdown Timer Python Project

import time

def countdown_timer(t: int) -> None:
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
    
        time.sleep(1)
        t -= 1
    print('Timer completed!')

countdown_timer(10)