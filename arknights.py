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


class ArknightsModule:
    def __init__(self, stamina=None):

        self.initial_run = True

        self.BUFFER_SHORT = 3
        self.BUFFER_LONG = 60
        self.BUFFER_TIME = 10

        self.stamina = stamina
        self.game_exe = 'C:\LD Player\LDPlayer\dnplayer.exe'
        
        self.game_ppid = 0
        self.game_pid = 0

        self.ran_day = -1

    def start_game(self):
        print("Starting game engine LDPlayer...")
        st = time.time()

        subprocess.Popen(self.game_exe)
        print("Game engine started...")
        time.sleep(30)
        
        import pyautogui
        pyautogui.moveTo(1780, 465, duration = 1) # on 2k screen
        pyautogui.click()
        time.sleep(1)

        print("Starting Arknights...")
        keyboard.press('A')
        time.sleep(45)

        keyboard.press('Z')
        time.sleep(30)

        print("Logging into Arknights...")
        keyboard.press('5')
        time.sleep(60)

        return time.time() - st

    def close_ads(self):
        st = time.time()

        print("Closing ads...")
        for _ in range(5):
            keyboard.press('X')
            time.sleep(self.BUFFER_SHORT * 2)

        print("Returning to home screen...")
        keyboard.press('K')
        time.sleep(1)
        keyboard.press('W')
        time.sleep(self.BUFFER_TIME)

        return time.time() - st

    def grind_resources(self):
        # starting from home screen
        with_timezone = datetime.now(pytz.timezone("HongKong"))
        wd = with_timezone.weekday() + 1
        money_grind = True if wd % 2 == 0 else False
        st = time.time()

        game_time = 150 if money_grind == True else 240
        STAMINA_REQ = 36

        print("Resource grind starting...")
        keyboard.press(';')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('\'')
        time.sleep(self.BUFFER_SHORT)

        if money_grind: keyboard.press('4')
        else: keyboard.press('2')
        time.sleep(self.BUFFER_SHORT)

        keyboard.press('R')
        time.sleep(self.BUFFER_SHORT)

        game_ct = 1
        while self.stamina > STAMINA_REQ:
            print(f"Starting game {game_ct}... (remaining stamina: {self.stamina})")
            game_ct += 1

            keyboard.press('A')
            time.sleep(self.BUFFER_TIME)

            keyboard.press('B')
            time.sleep(game_time)

            keyboard.press('U')
            time.sleep(self.BUFFER_TIME)

            keyboard.press('A')
            time.sleep(self.BUFFER_TIME)

            self.stamina -= STAMINA_REQ

        print("Exiting resource grind...")
        keyboard.press('K')
        time.sleep(1)
        keyboard.press('W')

        return time.time() - st

    def reload_base(self):
        # starting from home screen
        st = time.time()

        print("Initializing base...")
        keyboard.press('H')
        time.sleep(self.BUFFER_LONG)


        print("Entering stage 1 [residence one]...")
        keyboard.press('Q')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('W')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('E')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('R')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('1')
        keyboard.press('2')
        keyboard.press('3')
        keyboard.press('4')
        keyboard.press('5')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('T')
        time.sleep(self.BUFFER_TIME)


        print("Entering stage 2 [residence two]...")
        keyboard.press('Y')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('E')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('R')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('1')
        keyboard.press('2')
        keyboard.press('3')
        keyboard.press('4')
        keyboard.press('5')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('T')
        time.sleep(self.BUFFER_TIME)


        print("Entering stage 3 [residence three]...")
        keyboard.press('U')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('E')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('R')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('1')
        keyboard.press('2')
        keyboard.press('3')
        keyboard.press('4')
        keyboard.press('5')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('T')
        time.sleep(self.BUFFER_TIME)

        
        print("Entering stage 4 [trading station]...")
        keyboard.press('I')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('L')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('I')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('W')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('R')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('J') # clear selection
        keyboard.press('3')
        keyboard.press('5')
        keyboard.press('U')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('S')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('F')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('I')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('G')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('J') # clear selection
        keyboard.press('3')
        keyboard.press('5')
        keyboard.press('U')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('T')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('T')
        time.sleep(self.BUFFER_TIME)


        print("Entering stage 5 [factory station]...")
        keyboard.press('O')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('P')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('S')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('D')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('O')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('F')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('G')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('J') # clear selection
        keyboard.press('3')
        keyboard.press('5')
        keyboard.press('U')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('I')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('G')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('J') # clear selection
        keyboard.press('3')
        keyboard.press('5')
        keyboard.press('U')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('S')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('G')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('J') # clear selection
        keyboard.press('3')
        keyboard.press('5')
        keyboard.press('U')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('P')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('G')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('J') # clear selection
        keyboard.press('3')
        keyboard.press('5')
        keyboard.press('U')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('A')
        time.sleep(self.BUFFER_SHORT)
        keyboard.press('A')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('T')
        time.sleep(self.BUFFER_TIME)

        keyboard.press('T')
        time.sleep(self.BUFFER_TIME)

        print("Exiting base...")
        keyboard.press('K')
        time.sleep(1)
        keyboard.press('W')
        time.sleep(1)
        keyboard.press('U')
        time.sleep(self.BUFFER_LONG)

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

    def runtime_trigger(self):
        current_time = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
        day_time = current_time.split("-")

        # print(day_time)

        days = [int(d) for d in day_time[0].split("/")]
        time = [int(t) for t in day_time[1].split(":")]

        month = days[0]
        today = days[1]
        year = days[2]

        hour = time[0]
        min = time[1]
        sec = time[2]

        # Run first game now
        if self.initial_run == True:
            self.initial_run = False
            self.ran_day = today
            return True

        if hour == 20 and today != self.ran_day: # 8:00PM
            self.ran_day = today
            return True
        else:
            return False

# last key: X
if __name__ == "__main__":

    EXECUTION_TIME = 20
    RELOAD_BASE = True
    GRIND_RESOURCES = False

    print(f'========== CONFIGURATIONS ==========\nExecution time: {EXECUTION_TIME}:00 daily\nBase reload: {RELOAD_BASE}\nResource grind: {GRIND_RESOURCES}')
    i = input("\nRun arknights? [y/n]")
    if i.lower() != 'y': exit()
    
    while True:

        with open("stamina.json") as rf: st = json.load(rf)["stamina"]

        # initializing program
        arknights = ArknightsModule(st)
        print('Program starting in 3 sec...')
        time.sleep(arknights.BUFFER_TIME - 2)

        if arknights.runtime_trigger() == True:
            pass

            total_time = 0
            if arknights.validate_game_activity() == False:
                total_time += arknights.start_game()
                total_time += arknights.close_ads()
            if RELOAD_BASE: total_time += arknights.reload_base()
            if GRIND_RESOURCES: total_time += arknights.grind_resources()

            if arknights.validate_game_activity() == True:
                arknights.exit_game()

            print(f"\nArknights Module Execution Complete...\nTotal Time Taken: [{round(total_time, 2)}]")
            
            print("Sleeping for 3 hour...")
            time.sleep(3600 * 3)

        current_time = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
        try:
            if arknights.ran_day == -1:
                current_time = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
                day_time = current_time.split("-")
                days = [int(d) for d in day_time[0].split("/")]
                _time = [int(t) for t in day_time[1].split(":")]
                today = days[1]
                hour = _time[0]
                if hour >= EXECUTION_TIME: today += 1

                td = datetime.now().replace(day=today, hour=EXECUTION_TIME, minute=0, second=0) - datetime.now()
                print(f"[{current_time}] Time left till next run: {td}")
            else:
                td = datetime.now().replace(day=arknights.ran_day + 1, hour=EXECUTION_TIME, minute=0, second=0) - datetime.now()
                print(f"[{current_time}] Time left till next run: {td}")
        except:
            print(f"[{current_time}] error generating time for the next run...")
        time.sleep(random.randint(60, 120))
