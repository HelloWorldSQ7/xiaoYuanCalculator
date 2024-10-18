import math
import sys
import keyboard
from PIL import ImageGrab
import pyautogui
import cv2
import pytesseract

while True:
    if keyboard.is_pressed('space'):
        print("Game over")
        sys.exit()
    ImageGrab.grab(bbox=(100, 300, 450, 450)).save("num.png")
    pytesseract.pytesseract.tesseract_cmd = r"E:\xiaoYuanCalculator"
    img = cv2.imread("num.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(img, 150, 100, cv2.THRESH_BINARY)
    result = pytesseract.image_to_string(thresh, config="-- psm 6").split("?")
    try:
        result[0] = result[0].strip()
        result[1] = result[1].strip()
        if result[0] == "0":
            result[0] = 0
        if result[1] == "0":
            result[1] = 0
        num1 = math.floor(float(result[0]))
        num2 = math.floor(float(result[1]))
        pyautogui.moveTo(277,700, duration=0.1)
        if num1 > num2:
            pyautogui.mouseDown(100,100, duration=0.1)
            pyautogui.move(100,100, duration=0.1)
            pyautogui.mouseUp()
            print(f"{num1} > {num2}")
        else:
            pyautogui.mouseDown(100, 100, duration=0.1)
            pyautogui.move(100, 100, duration=0.1)
            pyautogui.mouseUp()
            print(f"{num1} < {num2}")
    except IndexError as e:
        print("No content captured")
    except ValueError as e:
        print("No content captured")

