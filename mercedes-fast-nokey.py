import pyautogui as pg

while (True):
    img = pg.locateAllOnScreen('./img/merc.png',confidence=0.84,region=(273,130,451,645))
    for point in img:
        if (point is not None):
            pg.click(pg.center(point))