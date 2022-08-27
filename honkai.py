import os
import sys
import time
import psutil
import ctypes
from ctypes import wintypes
import pyautogui
import pyautogui as keyboard
import time
import subprocess
import json

pyautogui.FAILSAFE = False

# RELOAD_BASE = True
# GRIND_RESOURCES = False

class honkaiModule:
    def __init__(self, stamina=0):

        self.initial_run = True

        self.BUFFER_SHORT = 10
        self.BUFFER_LONG = 90
        self.BUFFER_TIME = 25

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

        print("Starting honkai...")
        keyboard.press('D')
        time.sleep(300)


        print("Logging into honkai...")
        keyboard.press('A')
        time.sleep(60)

        return time.time() - st


    def attempt_update(self):
        st = time.time()

        print("Attempt Update...")
        keyboard.press('U')
        time.sleep(60)
        keyboard.press('V')
        time.sleep(self.BUFFER_TIME)

        return time.time() - st


    def close_ads(self):
        st = time.time()

        print("Closing B ads...")
        for _ in range(5):
            keyboard.press('B')
            time.sleep(self.BUFFER_TIME)

        print("Closing C ads...")
        for _ in range(5):
            keyboard.press('C')
            time.sleep(self.BUFFER_TIME)

        print("Closing B ads again...")
        for _ in range(5):
            keyboard.press('B')
            time.sleep(self.BUFFER_TIME)

        print("Closing C ads again...")
        for _ in range(5):
            keyboard.press('C')
            time.sleep(self.BUFFER_TIME)

        keyboard.press('H')
        return time.time() - st


    def reload_base(self):
        # starting from home screen
        st = time.time()

        print("Base reload starting...")
        time.sleep(self.BUFFER_TIME)
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


        keyboard.press('G')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('B')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('I')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('1')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('B')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('I')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('2')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('B')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('I')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('3')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('B')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('I')
        time.sleep(self.BUFFER_SHORT)


        # shifting down on page
        keyboard.keyDown('Z')
        time.sleep(1.72)
        keyboard.keyUp('Z')

        keyboard.press('G')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('B')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('I')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('1')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('B')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('I')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('2')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('B')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('I')
        time.sleep(self.BUFFER_SHORT)


        print(f"Returning to home screen...")
        keyboard.press('J')
        time.sleep(self.BUFFER_TIME)

        return time.time() - st


    def grind_resources(self):
        # starting from home screen
        st = time.time()

        STAMINA_REQ = 10

        print("Resource grind starting...")
        keyboard.press('K')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('L')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('M')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('L')
        time.sleep(self.BUFFER_TIME)


        # shifting down on page
        keyboard.keyDown('X')
        time.sleep(40)
        keyboard.keyUp('X')

        keyboard.keyDown('y')
        time.sleep(4.5)
        keyboard.keyUp('y')
        time.sleep(1)


        keyboard.press('P')
        time.sleep(self.BUFFER_SHORT)


        game_ct = 1
        while self.stamina > STAMINA_REQ:
            print(f"Starting game {game_ct}... (remaining stamina: {self.stamina - STAMINA_REQ})")
            game_ct += 1
            self.stamina -= STAMINA_REQ

            keyboard.press('D')
            time.sleep(self.BUFFER_SHORT)
            keyboard.press('D')


            time.sleep(30)

            keyboard.press('O')
            time.sleep(self.BUFFER_SHORT)
            keyboard.press('2')
            time.sleep(self.BUFFER_TIME)

            keyboard.press('O')
            time.sleep(self.BUFFER_SHORT)
            keyboard.press('2')
            time.sleep(self.BUFFER_TIME)

            keyboard.press('N')
            time.sleep(self.BUFFER_TIME)
            keyboard.press('D')
            time.sleep(self.BUFFER_TIME)


            if self.stamina > STAMINA_REQ: # continue to next game
                keyboard.press('P')
                time.sleep(self.BUFFER_SHORT)
            else:
                break
        
        # returning to home screen
        print("Exiting resource grind...")
        keyboard.press('H')
        time.sleep(self.BUFFER_TIME)
        keyboard.press('H')
        time.sleep(self.BUFFER_TIME)
        keyboard.press('J')
        time.sleep(self.BUFFER_TIME)

        return time.time() - st


    def get_daily_gifts(self):
        st = time.time()

        print("Getting daily gifts...")

        # gifts
        keyboard.press('Q')
        time.sleep(self.BUFFER_TIME)
        keyboard.press('R')
        time.sleep(self.BUFFER_TIME)
        keyboard.press('S')
        time.sleep(self.BUFFER_TIME)
        keyboard.press('T')
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


    def run_honkai(self):
        time.sleep(1)
        with open("honkai-stamina.json") as rf: 
            self.stamina = json.load(rf)["stamina"]
        
        print(f"Stamina: {self.stamina}")
        total_time = 0
        
        if self.validate_game_activity() == False:
            total_time += self.start_game()
            total_time += self.close_ads()
            total_time += self.attempt_update()
            total_time += self.close_ads() # close ads again after update attempt
            total_time += self.reload_base()
            total_time += self.grind_resources()
            total_time += self.get_daily_gifts()
            
            if self.validate_game_activity() == True:
                self.exit_game()
        
        print(f"\Honkai Module Execution Complete...\nTotal Time Taken: [{round(total_time, 2)}]")


# last key: X
if __name__ == "__main__":
    honkai = honkaiModule()
    honkai.run_honkai()

