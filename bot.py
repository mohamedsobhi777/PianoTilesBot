import pyautogui
import time
from mss import mss

start_x = 330
start_y = 590
pyautogui.PAUSE = 0
bbox = (start_x, start_y, start_x+600, start_y + 10)

cords_x = [50,200,400,500]


def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(bbox)
        t2 = time.time()
        print(t2 - t1)

def print_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)

def start():
    ok = 1
    strikes = 0
    with mss()  as sct:
        while ok == 1:
            time.sleep(0.001)
            img = sct.grab(bbox)
            cnt = 0
            for cord in cords_x:
                if img.pixel(cord,0) == (0,0,0) and img.pixel(cord,5) == (0,0,0):
                    cnt = cnt + 1
            if cnt > 2:
                ok = 0
            for cord in cords_x:
                shoot = 1
                img = sct.grab(bbox)
                for j in range(30):
                    if img.pixel(cord + j,0) != (0,0,0)  or img.pixel(cord + j,2)!= (0,0,0) or img.pixel(cord + j,3) != (0,0,0)or img.pixel(cord + j,8) != (0,0,0):
                        shoot = 0
                        break
                if shoot:
                    img = sct.grab(bbox)
                    if(img.pixel(cord,1) == (0,0,0)):
                        pyautogui.click(start_x + cord , start_y + 1)
                    break
start()
