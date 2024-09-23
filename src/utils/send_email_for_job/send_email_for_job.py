import os
from dotenv import load_dotenv

import pyautogui
from time import sleep
import keyboard

load_dotenv()

curriculums_path = os.getenv("PATH_WHERE_CURRICULUMS")


def send_email_for_job(job):
    
    email = job[0]
    tech = job[1]
    details_job = job[2]
    
    msg = f"""Prezada Equipe de RH,

Gostaria de me candidatar à vaga de Desenvolvedor de Software {details_job}. Com sólida experiência em desenvolvimento de software, acredito que posso contribuir significativamente para a equipe.
Anexo meu currículo para sua apreciação. Estou à disposição para uma entrevista e maiores esclarecimentos.

Agradeço a oportunidade.
"""
    
    image_email_path = os.path.join(os.getcwd(), 'assets', 'email.png')
    # position_email_select = pyautogui.locateCenterOnScreen(image_email_path)
    
    # pyautogui.click(233,316, duration=0.2)
    # # sleep(2)
    pyautogui.click(227,350, duration=0.3)
    sleep(2)
    pyautogui.click(161,134, duration=0.5)
    sleep(2)
    pyautogui.click(561,263, duration=1)
    pyautogui.write(email, interval=0.03)
    pyautogui.click(473,326, duration=0.2)
    pyautogui.write(f"Candidatura para Vaga de {details_job}", interval=0.03)
    pyautogui.click(482,397, duration=0.2)
    keyboard.write(msg, 0.01)
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
    if technology == 'Java':
        pyautogui.doubleClick(361,232, duration=0.2)
    if technology == 'Javascript Frontend':
        pyautogui.doubleClick(349,266, duration=0.2)
    if technology == 'Javascript Fullstack':
        pyautogui.doubleClick(370,342, duration=0.2)
    if technology == 'Python':
        pyautogui.doubleClick(463,378, duration=0.2)
    sleep(3)
    pyautogui.click(496,193, duration=0.2)
    
    write_to_log(f'E-mail: {email} sent sucessfully')
    
    return True
