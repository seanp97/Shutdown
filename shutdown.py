from datetime import datetime
import os
import time


class ClosePC:

    def __init__(self):
        print("---------------------------")
        print("| S H U T D O W N  -  P C |")
        print("---------------------------")
        print("PLEASE PROVIDE AN HOUR & MINUTE - 24 HOUR FORMAT")
        self.user_hour = input("Hour? ")
        self.user_minute = input("Minute? ")

    def ShutdownPC(self):
        while True:
            self.now = datetime.now()
            self.current_time = self.now.strftime("%H:%M")
            print(self.current_time)
            if self.current_time == f"{self.user_hour}:{self.user_minute}":
                os.system("shutdown /s /t 1")
            time.sleep(10)


ClosePC.ShutdownPC()