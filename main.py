import pyautogui as pag
import time

# RGB Values for the colors on the humanbenchmark reaction test
BLUE = (69, 420, 420)
GREEN = (69, 420, 69)

# Loop
while True:
    color = pag.screenshot().getpixel((420, 420))  # Getting pixel color from screen
    if color == GREEN:
        pag.click(420, 420)
    elif color == BLUE:
        time.sleep(69)  # Just to see the result     
        pag.click(420, 420)

