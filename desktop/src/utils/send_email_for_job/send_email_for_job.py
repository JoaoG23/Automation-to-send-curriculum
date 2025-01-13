import os
from dotenv import load_dotenv
import random

import pyautogui
from time import sleep
import keyboard

from src.utils.logging.log_manager.log_manager import write_to_log
from src.utils.send_email_for_job import MESSAGES_BODY

load_dotenv()

curriculums_path = os.getenv("PATH_WHERE_CURRICULUMS")

def send_email_for_job(job):
    
    email = job[0]
    tech = job[1]
    details_job = job[2]
    salary = job[3]
    message = ""
    message_random_salary = random.choice(MESSAGES_BODY.MESSAGES_BODY_WITH_SALARY)
    message_salary_replaced = message_random_salary.replace("((details_job))", details_job).replace("((salary))", salary)
    message = message_salary_replaced
    
    if salary == "":
        message_random_without_salary = random.choice(MESSAGES_BODY.MESSAGES_BODY_WITHOUT_SALARY)
        message_without_salary_replaced = message_random_without_salary.replace("((details_job))", details_job)
        message = message_without_salary_replaced
    # image_email_path = os.path.join(os.getcwd(), 'assets', 'email.png')
    # position_email_select = pyautogui.locateCenterOnScreen(image_email_path)
    pyautogui.click(227,350, duration=0.3)
    sleep(2)
    pyautogui.click(161,134, duration=0.5)
    sleep(2)
    pyautogui.click(561,263, duration=1)
    pyautogui.write(email, interval=0.03)
    pyautogui.click(473,326, duration=0.2)
    keyboard.write(f"Candidatura para Vaga de {details_job}", 0.03)
    pyautogui.click(482,397, duration=0.2)
    keyboard.write(message, 0.01)
    sleep(1)
    
    pyautogui.click(607,78, duration=0.4)
    pyautogui.click(192,133, duration=0.6)
    pyautogui.click(137,174, duration=0.6)
    sleep(1)
    pyautogui.click(555,67, duration=0.6)
    sleep(2)
    pyautogui.write("", interval=0.01)
    sleep(1)
    keyboard.write(curriculums_path, 0.010)
    sleep(1)
    pyautogui.click(642,67, duration=0.1)
    technology = tech
    sleep(3)
    pyautogui.click(251,518, duration=0.2)
    sleep(2)
    if technology == 'java':
        keyboard.write("joao-guilherme-desenvolvedor-java", 0.03)
    if technology == 'frontend':
        keyboard.write("joao-guilherme-desenvolvedor-frontend", 0.03)
    if technology == 'fullstack':
        keyboard.write("joao-guilherme-desenvolvedor-JS-fullstack", 0.03)
    if technology == 'node':
        keyboard.write("joao-guilherme-desenvolvedor-JS-backend", 0.03)
    if technology == 'python':
        keyboard.write("joao-guilherme-desenvolvedor-python", 0.03)
    sleep(2)
    pyautogui.click(731,548, duration=0.2)
    sleep(7)
    pyautogui.click(496,193, duration=0.2)
    
    write_to_log(f'E-mail: {email} sent sucessfully')
    
    return True
