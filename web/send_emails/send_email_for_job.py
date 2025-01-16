import os
from dotenv import load_dotenv
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from send_emails.add_attachment_resume.add_attachment_resume import add_attachment_resume
from send_emails.add_footer.add_footer import add_footer
from send_emails.prepare_to_body_email.prepare_to_body_email import prepare_to_body_email
from utils.logging.log_manager.log_manager import write_to_log

load_dotenv()

name_candidate = os.getenv("NAME_CANDIDATE")

def wait_for_element_load_it(element, name_elemento):
    sleep(1)
    while len(element) < 1:
        print(f"{name_elemento} loading......")
        sleep(2)
    print(f"{name_elemento} element found.")
    sleep(1)
    first_element = element[0]
    return first_element
    
        
def send_email_for_job(driver, job, index):
    
    email = job[0]
    tech = job[1]
    details_job = job[2]
    recruiter = job[4] or 'Recrutador(a)'
    
    text_body = prepare_to_body_email(job)

    sleep(10)
    new_email_button = wait_for_element_load_it(
        driver.find_elements(By.XPATH, "//*[text()='Novo email']"), 
                          'button new email'                      
    )
    new_email_button.click()
    sleep(1)
    destination_email_input = wait_for_element_load_it(
        driver.find_elements(By.XPATH, f'//*[@id="docking_InitVisiblePart_{index}"]/div/div[3]/div[1]/div/div[2]/div/span/span[2]/div/div[1]'), 
                          'field destination email')
    
    sleep(1)
    destination_email_input.send_keys(email)
    
    sleep(1)
    subject_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="docking_InitVisiblePart_{index}"]/div/div[3]/div[2]/span/input')) 
    )
    sleep(1)
    subject_input.send_keys(f"Candidatura de {name_candidate} referente a vaga para {details_job}")
    
    sleep(1)
    sequence_id_body = index + 1
    body_textarea = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="editorParent_{sequence_id_body}"]/div')) 
    )
    sleep(1)
    body_textarea.send_keys(text_body)
    
    sleep(1)
    add_footer(driver, sequence_id_body)
    
    sleep(1)
    add_attachment_resume(driver, tech)
    # send_email_button = driver.find_element(By.XPATH, "//*[@title='Enviar (Ctrl+Enter)']")
    send_email_button  = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@title='Enviar (Ctrl+Enter)']"))
    )
    
    sleep(2)
    send_email_button.click()
    sleep(2)
    write_to_log(f'E-mail: {email} sent sucessfully, Recruiter: {recruiter}, Techonology: {tech}')
    
    return True
