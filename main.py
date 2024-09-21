import os
from dotenv import load_dotenv
import csv

from src.utils.send_email_for_job.send_email_for_job import send_email_for_job
# import pyautogui
# from time import sleep

# load_dotenv()

# curriculums_path = os.getenv("PATH_WHERE_CURRICULUMS")
# pyautogui.moveTo(50, 100, duration=2) 


# 985,1060
# 228,448
# 218,487
# 161,134
# 561,263
# email
# 473,326
# Assunto
# 482,397
# Pra quem palavras chaves  replace
# 607,78
# 192,133
# 137,174

# Seleciona arquivos
# 361,232 * 2 - para java
# 349,266 * 2 - para js frontend
# 370,342 * 2 - para js fullstack

# 496,193
if __name__ == '__main__':
    try:
        
        path_imports = os.path.join(os.getcwd(), 'imports', 'jobs.csv')

        with open(path_imports, 'r') as file:
            file_read = csv.reader(file, delimiter=';')
            
            ## Remove header
            
            for row in file_read:
                # print(row)
                send_email_for_job(row)
    
    except Exception as e:
        print(e)