import pyautogui as pg
import time

def run():
    t = time.time()
    while (time.time() < t + 31):
        img = pg.locateAllOnScreen('./img/merc.png',confidence=0.84,region=(273,130,451,645))
        for point in img:
            if (point is not None):
                pg.click(pg.center(point))

while (True):
    point = pg.locateOnScreen('./img/again.png')
    if (point is not None):
        pg.click(pg.center(point))
        run()
