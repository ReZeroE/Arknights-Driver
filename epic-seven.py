import os
import sys
import time
import psutil
import ctypes
from ctypes import wintypes
import pyautogui as keyboard
import datetime
from datetime import datetime
import time
import pytz
import subprocess
import json
import random


EXECUTION_TIME = 8
RELOAD_BASE = True
GRIND_RESOURCES = False

class EpicSevenModule:
    def __init__(self, stamina=0):

        self.initial_run = True

        self.BUFFER_SHORT = 3
        self.BUFFER_LONG = 60
        self.BUFFER_TIME = 15

        self.stamina = stamina
        self.game_exe = 'D:\LDPlayer9\dnplayer.exe'
        
        self.game_ppid = 0
        self.game_pid = 0

        self.ran_day = -1

    def start_game(self):
        print("Starting game engine LDPlayer...")
        st = time.time()

        subprocess.Popen(self.game_exe)
        print("Game engine started...")
        # time.sleep(150)
        
        import pyautogui
        pyautogui.moveTo(1743, 462, duration = 1) # on 2k screenC
        pyautogui.click()
        time.sleep(3)

        print("Starting EpicSeven...")
        keyboard.press('C')
        time.sleep(60)

        print("Logging into EpicSeven...")
        keyboard.press('A')
        time.sleep(60)


        return time.time() - st


    def close_ads(self):
        st = time.time()

        print("Closing B ads...")
        for _ in range(10):
            keyboard.press('B')
            time.sleep(self.BUFFER_TIME)
        
        time.sleep(5)

        print("Closing C ads...")
        for _ in range(5):
            keyboard.press('C')
            time.sleep(self.BUFFER_TIME)

        return time.time() - st


    def grind_resources(self):
        # starting from home screen
        st = time.time()

        GAME_TIME = 360

        keyboard.press('E')
        time.sleep(1)

        print("Resource grind starting...")
        keyboard.press('F')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('C')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('G')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('G')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('H')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('H')
        time.sleep(GAME_TIME)


        # keyboard.press('A')
        # time.sleep(self.BUFFER_SHORT)
        # keyboard.press('H')
        # time.sleep(self.BUFFER_TIME)
        
        # returning to home screen
        # keyboard.press('J')
        # time.sleep(self.BUFFER_TIME)
        # keyboard.press('K')
        # time.sleep(self.BUFFER_TIME)

        print("Exiting resource grind...")
        time.sleep(1)

        return time.time() - st


    def get_daily_gifts(self):
        st = time.time()

        print("Getting daily gifts...")

        # gifts
        keyboard.press('E')
        time.sleep(1)

        keyboard.press('B')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('C')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('D')
        time.sleep(1)

        keyboard.press('D')
        time.sleep(self.BUFFER_TIME)

        return time.time() - st


    def validate_game_activity(self):
        user32 = ctypes.windll.user32

        h_wnd = user32.GetForegroundWindow()
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
        # print(pid.value)
        pid = psutil.Process(pid.value)

        # print(pid.exe())
        if pid.exe() == self.game_exe:
            self.game_pid = pid.pid
            self.game_ppid = pid.ppid()
            return True
        else:
            print("window unfocused, starting game...")
            return False

    def exit_game(self):
        time.sleep(10)

        #taskkill /F /PID pid_number
        output = subprocess.getoutput(f"taskkill /F /PID {self.game_pid}")
        print(f"Exiting game...\n{output}")


    def run_epic_seven(self):
        time.sleep(1)
        with open("epic-seven-stamina.json") as rf: 
            self.stamina = json.load(rf)["stamina"]
        
        print(f"Stamina: {self.stamina}")
        total_time = 0
        # if self.validate_game_activity() == False:
        #     total_time += self.start_game()
            # total_time += self.close_ads()
            # total_time += self.grind_resources()
            # total_time += self.get_daily_gifts()
            
            # if self.validate_game_activity() == True:
            #     self.exit_game()
        
        # self.start_game()
        # self.get_daily_gifts()
        self.grind_resources()


        print(f"\EpicSeven Module Execution Complete...\nTotal Time Taken: [{round(total_time, 2)}]")


# last key: X
if __name__ == "__main__":

    EpicSeven = EpicSevenModule()
    EpicSeven.run_epic_seven()
            
