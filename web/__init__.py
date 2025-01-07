import os
import csv
import traceback

from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

# from web.utils.logging.log_manager import write_to_log

# from web.utils.logging.log_manager.log_manager import write_to_log
from utils.logging.log_manager.log_manager import write_to_log
from utils.send_email_for_job.send_email_for_job import send_email_for_job
from utils.move_to_file.move_to_file import move_to_file


# user_profile = "C:\\Users\\joaog\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

# options.add_argument(f"user-data-dir={user_profile}")
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

if __name__ == '__main__':
    try:
        
        
        # pyautogui.PAUSE = 1
        # pyautogui.position()
        # icon_navbar_path = os.path.join(os.getcwd(), 'assets', 'icon_navbar.png')
        # icon_navbar_position = pyautogui.locateCenterOnScreen(icon_navbar_path , grayscale=True, confidence=.7)
        # pyautogui.click(icon_navbar_position, duration=0.3)
        # sleep(10)
        
        # pyautogui.keyDown('winleft')
        # pyautogui.press('up')
        # pyautogui.keyUp('winleft')
        # sleep(1)
        
        # # image_email_path = os.path.join(os.getcwd(), 'assets', 'email.png')
        # # email_select_position = pyautogui.locateCenterOnScreen(image_email_path , grayscale=True, confidence=.9)
        
        # pyautogui.click(231,322, duration=0.2)
        # sleep(2)
        
        datetime_now = datetime.now().strftime('%Y%m%d%H%M%S')
        
        path_file_imports = os.path.join(os.getcwd(), 'import', 'jobs.csv')
        path_file_export = os.path.join(os.getcwd(), 'exported', datetime_now +'.csv')

        with open(path_file_imports, 'r') as file:
            file_read = csv.reader(file, delimiter=';')
            list_file = list(file_read) 
            list_file.pop(0)
            
            for row in list_file:
                print("🚀 ~ row:", row)
                # send_email_for_job(row)
                
        sleep(2)
        
        move_to_file(path_file_imports, path_file_export)
        # write_to_log(f'Curriculums sent with success!{len(list_file)}')
    except WebDriverException as e:
        write_to_log(f"WebDriverException: {traceback.format_exc()}", type='error')
        print(f"Erro ao rodar webdriver")
    except Exception as e:
        write_to_log(f"Exception: {traceback.format_exc()}", type='error')
        print(f"Erro ao rodar automação")
    finally:
        print("Encerrando automação")
        driver.quit()   
    # except KeyboardInterrupt as e:
    #     print("KeyboardInterrupt : Interrupted by user.")
    #     write_to_log(f"KeyboardInterrupt: {traceback.format_exc()}", type='error')
    # except ImageNotFoundException as e:
    #     print("ImageNotFoundException : Image not found.")
    #     write_to_log(f"ImageNotFoundException: {traceback.format_exc()}", type='error')
    # except Exception as e:
    #     print("RuntimeError : An error occurred on app.")
    #     write_to_log(f"Error {traceback.format_exc()}", type='error')