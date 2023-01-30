import pyautogui as pg

pg.FAILSAFE = True

point = (1806, 725)


while True:
    pg.click(point, interval=0.05)
    if pg.press("f11"):
        break

