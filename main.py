import os
import csv

import pyautogui
from time import sleep

from src.utils.logging.log_manager.log_manager import write_to_log
from src.utils.send_email_for_job.send_email_for_job import send_email_for_job

if __name__ == '__main__':
    try:
        
        
        icon_navbar_path = os.path.join(os.getcwd(), 'assets', 'icon_navbar.png')
        icon_navbar_position = pyautogui.locateCenterOnScreen(icon_navbar_path)
        pyautogui.click(icon_navbar_position, duration=0.3)
        sleep(10)

        
        image_email_path = os.path.join(os.getcwd(), 'assets', 'email.png')
        email_select_position = pyautogui.locateCenterOnScreen(image_email_path)
        
        pyautogui.click(email_select_position, duration=0.1)
        sleep(2)
        
        path_imports = os.path.join(os.getcwd(), 'imports', 'jobs.csv')

        with open(path_imports, 'r') as file:
            file_read = csv.reader(file, delimiter=';')
            list_file = list(file_read) 
            list_file.pop(0)
            
            for row in list_file:
                send_email_for_job(row)
                
        sleep(1)
        pyautogui.click(1889,22, duration=0.6)
        
        write_to_log(f'Curriculums sent with success!{len(list_file)}')
    except Exception as e:
        write_to_log(f"Error to run the program: {e}", type='error')