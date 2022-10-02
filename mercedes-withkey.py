import pyautogui as pg
from pynput import keyboard as kb

break_program = False

def on_press(key):
    global break_program
    if key == kb.Key.end:
        print("end pressed")
        break_program = True
        return False

with kb.Listener(on_press = on_press) as listener:
    while (break_program == False):
        img = pg.locateAllOnScreen('./img/merc.png',
        confidence=0.8812,
        region=(273,130,451,645))

        for point in img:
            if (point is not None):
                print(point)
                pg.click(pg.center(point))

        point = pg.locateOnScreen('./img/again.png')
        if (point is not None):
            pg.click(pg.center(point))
        

    listener.join()

