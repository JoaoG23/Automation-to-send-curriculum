import os
import csv
from tkinter import *
import traceback

import pyautogui
from pyautogui import ImageNotFoundException
from time import sleep
from datetime import datetime


from src.utils.logging.log_manager.log_manager import write_to_log
from src.utils.send_email_for_job.send_email_for_job import send_email_for_job
from src.utils.move_to_file.move_to_file import move_to_file

if __name__ == '__main__':
    try:
        
        
        pyautogui.FAILSAFE = False
        # pyautogui.PAUSE = 1
        # pyautogui.position()
        icon_navbar_path = os.path.join(os.getcwd(), 'assets', 'icon_navbar.png')
        icon_navbar_position = pyautogui.locateCenterOnScreen(icon_navbar_path , grayscale=True, confidence=.7)
        pyautogui.click(icon_navbar_position, duration=0.3)
        sleep(10)
        
        pyautogui.keyDown('winleft')
        pyautogui.press('up')
        pyautogui.keyUp('winleft')
        sleep(1)
        
        # image_email_path = os.path.join(os.getcwd(), 'assets', 'email.png')
        # email_select_position = pyautogui.locateCenterOnScreen(image_email_path , grayscale=True, confidence=.9)
        
        pyautogui.click(231,322, duration=0.2)
        sleep(2)
        
        datetime_now = datetime.now().strftime('%Y%m%d%H%M%S')
        
        path_file_imports = os.path.join(os.getcwd(), 'import', 'jobs.csv')
        path_file_export = os.path.join(os.getcwd(), 'exported', datetime_now +'.csv')

        with open(path_file_imports, 'r') as file:
            file_read = csv.reader(file, delimiter=';')
            list_file = list(file_read) 
            list_file.pop(0)
            
            for row in list_file:
                send_email_for_job(row)
                
        sleep(2)
        pyautogui.click(1889,22, duration=0.6)
        
        move_to_file(path_file_imports, path_file_export)
        write_to_log(f'Curriculums sent with success!{len(list_file)}')
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt : Interrupted by user.")
        write_to_log(f"KeyboardInterrupt: {traceback.format_exc()}", type='error')
    except ImageNotFoundException as e:
        print("ImageNotFoundException : Image not found.")
        write_to_log(f"ImageNotFoundException: {traceback.format_exc()}", type='error')
    except Exception as e:
        print("RuntimeError : An error occurred on app.")
        write_to_log(f"Error {traceback.format_exc()}", type='error')