
import os
import csv
import traceback

from time import sleep
from dotenv import load_dotenv
from datetime import datetime

from httpcore import TimeoutException
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSelectorException

from send_emails.send_email_for_job import send_email_for_job
from send_emails.update_line_csv_to_email_sended.update_line_csv_to_email_sended import update_line_csv_to_email_sended
from send_emails.verify_email_sent_by_line_csv.verify_email_sent_by_line_csv import verify_email_sent_by_line_csv
from utils.logging.log_manager.log_manager import write_to_log
from utils.move_to_file.move_to_file import move_to_file


# User profile path
edge_user_profile = os.getenv("EDGE_USER_PROFILE")

# Edge options
edge_options = webdriver.EdgeOptions()
edge_options.add_argument(f"user-data-dir={edge_user_profile}")
# edge_options.add_argument("--headless==new")
edge_service = EdgeService(EdgeChromiumDriverManager().install())

# Initialize Edge driver
driver = webdriver.Edge(service=edge_service, options=edge_options)

load_dotenv()

email_sender = os.getenv("EMAIL_USER")
password_sender = os.getenv("PASSWORD_USER")

## Utils
def wait_for_element_load(element, name_elemento):
    while len(element) < 1:
        print(f"wait for {name_elemento} element load.")
        sleep(2)
    print(f"Name {name_elemento} element found.")

    
if __name__ == '__main__':
    try:
    
        driver.maximize_window()
        sleep(1)
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=169&ct=1736367757&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26deeplink%3dowa%252f%253frealm%253dlive.com%26RpsCsrfState%3dccfc583d-fe0f-afde-5abd-826f8ab7a1c8&id=292841&aadredir=1&whr=live.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
        sleep(8)
        datetime_now = datetime.now().strftime('%Y%m%d%H%M%S')
        
        path_file_imports = os.path.join(os.getcwd(), 'import', 'jobs.csv')
        path_file_export = os.path.join(os.getcwd(),'exported', datetime_now +'.csv')

        with open(path_file_imports, 'r', encoding='utf-8') as file:
            file_read = csv.reader(file, delimiter=';')
            list_file = list(file_read) 
            list_file.pop(0)
            
            index_box_message_email = 0
            for i,row in enumerate(list_file):
                
                if not verify_email_sent_by_line_csv(i):
                    send_email_for_job(driver, row, index_box_message_email)
                    
                    update_line_csv_to_email_sended(i)
                    
                    index_box_message_email += 1
        sleep(2)
        
        move_to_file(path_file_imports, path_file_export)
        write_to_log(f'Resumes sent with success!{index_box_message_email}')
    except WebDriverException as e:
        write_to_log(f"WebDriverException: {traceback.format_exc()}", type='error')
    except InvalidSelectorException as e:
        write_to_log(f"InvalidSelectorException: {traceback.format_exc()}", type='error')
    except TimeoutException as e:
        write_to_log(f"TimeoutException: {traceback.format_exc()}", type='error')
    except Exception as e:
        write_to_log(f"Exception: {traceback.format_exc()}", type='error')
    finally:
        print("Encerrando automação")
        driver.quit()   