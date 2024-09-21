import os
from dotenv import load_dotenv

import pyautogui
from time import sleep

load_dotenv()

curriculums_path = os.getenv("PATH_WHERE_CURRICULUMS")

def send_email_for_job(job):
    
    email = job[0]
    recruiter_name = job[1]
    tech = job[2]
    details = job[3]
    
    msg = f"""
Prezada Equipe de RH,

Gostaria de me candidatar à vaga de Desenvolvedor de Software {details}. Com sólida experiência em desenvolvimento de software, acredito que posso contribuir significativamente para a equipe.
Anexo meu currículo para sua apreciação. Estou à disposição para uma entrevista e maiores esclarecimentos.

Agradeço a oportunidade.
"""
    
    
    try:
        pyautogui.FAILSAFE = False

        pyautogui.click(985,1060, duration=1)
        sleep(8)
        pyautogui.click(228,440, duration=1)
        sleep(2)
        pyautogui.click(218,487, duration=0.3)
        sleep(2)
        pyautogui.click(161,134, duration=0.5)
        sleep(2)
        pyautogui.click(561,263, duration=1)

        pyautogui.write(email, interval=0.03)
        pyautogui.click(473,326, duration=0.4)
        pyautogui.write(f"Candidatura para Vaga de {details}", interval=0.03)
        pyautogui.click(482,397, duration=0.4)
        pyautogui.write(msg.encode("utf-8"), interval=0.03)
        pyautogui.click(607,78, duration=0.4)
        pyautogui.click(192,133, duration=0.6)
        pyautogui.click(137,174, duration=0.6)
        pyautogui.click(473,61, duration=0.6)
        sleep(1)
        pyautogui.write("", interval=0.01)
        sleep(1)
        pyautogui.write(curriculums_path, interval=0.02)

        technology = 'Java'
        sleep(1)
        if technology == 'Java':
            pyautogui.doubleClick(361,232, duration=0.6)
        if technology == 'Javascript Frontend':
            pyautogui.doubleClick(349,266, duration=0.6)
        if technology == 'Javascript Fullstack':
            pyautogui.doubleClick(370,342, duration=0.6)
        sleep(3)
        pyautogui.moveTo(496,193, duration=0.6)
        sleep(1)
        pyautogui.moveTo(1889,22, duration=0.6)
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")