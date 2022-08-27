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

class KonosubaModule:
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
        time.sleep(150)
        
        import pyautogui
        pyautogui.moveTo(1743, 462, duration = 1) # on 2k screen
        pyautogui.click()
        time.sleep(3)

        print("Starting Konosuba...")
        keyboard.press('A')
        time.sleep(60)

        print("Logging into Konosuba...")
        keyboard.press('A')
        time.sleep(60)

        print("Attempting game update...")
        keyboard.press('E')
        time.sleep(3)
        keyboard.press('E')
        time.sleep(360)
        keyboard.press('E')
        time.sleep(3)
        keyboard.press('A')

        return time.time() - st


    def close_ads(self):
        st = time.time()

        print("Closing B ads...")
        for _ in range(10):
            keyboard.press('B')
            time.sleep(self.BUFFER_TIME)
        
        time.sleep(5)

        for _ in range(5):
            keyboard.press('O')
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

        STAMINA_REQ = 15
        GAME_TIME = 100

        print("Resource grind starting...")
        keyboard.press('D')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('E')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('F')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('G')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('H')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('I')

        game_ct = 1
        while self.stamina > STAMINA_REQ:
            print(f"Starting game {game_ct}... (remaining stamina: {self.stamina - STAMINA_REQ})")
            game_ct += 1
            self.stamina -= STAMINA_REQ

            time.sleep(GAME_TIME)

            keyboard.press('A')
            time.sleep(self.BUFFER_TIME)

            keyboard.press('A')
            time.sleep(self.BUFFER_TIME)

            keyboard.press('A')
            time.sleep(self.BUFFER_TIME)

            keyboard.press('A')
            time.sleep(self.BUFFER_SHORT)
            keyboard.press('F')
            time.sleep(self.BUFFER_TIME)


            if self.stamina > STAMINA_REQ: # continue to next game
                keyboard.press('A')
                time.sleep(self.BUFFER_SHORT)
                keyboard.press('E')
                time.sleep(self.BUFFER_TIME)
            else:
                break
        
        # returning to home screen
        keyboard.press('J')
        time.sleep(self.BUFFER_TIME)
        keyboard.press('K')
        time.sleep(self.BUFFER_TIME)

        print("Exiting resource grind...")
        time.sleep(1)

        return time.time() - st


    def get_daily_gifts(self):
        st = time.time()

        print("Getting daily gifts...")

        # gifts
        keyboard.press('L')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('J')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('J')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('J')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('M')
        time.sleep(self.BUFFER_SHORT)


        # mission
        keyboard.press('N')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('J')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('J')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('J')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('M')
        time.sleep(self.BUFFER_SHORT)

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


    def run_konosuba(self):
        time.sleep(1)
        with open("konosuba-stamina.json") as rf: 
            self.stamina = json.load(rf)["stamina"]
        
        print(f"Stamina: {self.stamina}")
        total_time = 0
        if self.validate_game_activity() == False:
            total_time += self.start_game()
            total_time += self.close_ads()
            total_time += self.grind_resources()
            total_time += self.get_daily_gifts()
            
            if self.validate_game_activity() == True:
                self.exit_game()
        
        print(f"\Konosuba Module Execution Complete...\nTotal Time Taken: [{round(total_time, 2)}]")


# last key: X
if __name__ == "__main__":

    konosuba = KonosubaModule()
    konosuba.run_konosuba()
            
