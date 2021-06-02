from pywinauto.application import Application 
from pywinauto import mouse, keyboard
import time
import pytesseract
import pyautogui as pag
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

app = Application(backend="uia").connect(title_re=".*Minecraft 1.16.4*")
mc = app.top_window()

#Fishing
#subtitles are at (1038, 611, 254, 876)
mc.type_keys('{ESC}')
time.sleep(1)
keep_fishing = True
while keep_fishing:
    # Cast
    pag.click(button='right') 
    wait_for_fish = True
    while wait_for_fish:
        img = pag.screenshot(region=(1038,611,750,400))
        #regions = [(611, 1038, 254, 876)]
        text =  pytesseract.image_to_string(img, lang='mc') 
        if 'splashes' in text:
            #print('Reel it in!')
            pag.click(button='right')
            time.sleep(2)
            wait_for_fish = False