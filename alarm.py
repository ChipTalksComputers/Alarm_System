import psutil
import time
import os
import sys


def checkProcesses(processName):

    for proc in psutil.process_iter():
        try:
            if processName in proc.name():
                return True
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

time_interval = 1

while(1):
    if (checkProcesses('chrome.exe')):
        time.sleep(5)
        if time_interval == 1:
            os.system('cmd /c "msg win10 You have been using chrome for long"')
            time_interval += 1
        elif time_interval == 2:
            os.system('cmd /c "msg win10 Ending process in 5 seconds"')
            time_interval += 1
        else:
            os.system('taskkill /F /IM chrome.exe')
            sys.exit()
            
        
        
