import os
import time
import pyautogui

class ScreenshotModule:

    def take_screenshot(self):
        MAIN_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'screenshots/')
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(MAIN_IMAGE_PATH + 'name.png')


if __name__ == "__main__":
    time.sleep(3)
    sm = ScreenshotModule()
    sm.take_screenshot()