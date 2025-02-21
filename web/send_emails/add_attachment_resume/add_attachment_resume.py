import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

def add_attachment_resume(driver, technology):
    main_path = os.getenv("PATH_WHERE_RESUMES")
    
    sleep(7)
    attachment_file = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,  "input[type='file']:nth-of-type(2)")) 
    )
    sleep(6)
    if technology == 'java':
        attachment_file.send_keys(main_path + "\\joao-guilherme-desenvolvedor-java.pdf")
        sleep(7)
    if technology == 'frontend':
        attachment_file.send_keys(main_path + "\\joao-guilherme-desenvolvedor-frontend.pdf")
        sleep(7)
    if technology == 'fullstack':
        attachment_file.send_keys(main_path + "\\joao-guilherme-desenvolvedor-JS-fullstack.pdf")
        sleep(7)
    if technology == 'node':
        attachment_file.send_keys(main_path + "\\joao-guilherme-desenvolvedor-JS-backend.pdf")
        sleep(7)
    if technology == 'python':
        attachment_file.send_keys(main_path + "\\joao-guilherme-desenvolvedor-python.pdf")
        sleep(7)
    sleep(10)
    