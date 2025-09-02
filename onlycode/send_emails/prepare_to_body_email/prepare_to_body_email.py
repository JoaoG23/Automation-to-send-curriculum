import random
import os
from send_emails.get_text_from_file.get_text_from_file import get_text_from_file

def prepare_to_body_email(job, path_templates_body: str):
    print(f"path_templates_body: {path_templates_body}")
    
    details_job = job[2]
    salary = job[3]
    recruiter = job[4] or 'Recrutador(a)' 
    
    message = ""
    
    # Usar caminhos relativos corretos
    if salary == "":
        path_body_without_salary = os.path.join(path_templates_body, "body_without_salary.txt")
        message_random_without_salary = get_text_from_file(path_body_without_salary)
        message_without_salary_replaced = message_random_without_salary.replace("((details_job))", details_job).replace("((recruiter))", recruiter)
        message = message_without_salary_replaced
    else:
        path_body_with_salary = os.path.join(path_templates_body, "body_with_salary.txt")
        message_random_salary = get_text_from_file(path_body_with_salary)
        message_salary_replaced = message_random_salary.replace("((details_job))", details_job).replace("((salary))", salary).replace("((recruiter))", recruiter)
        message = message_salary_replaced
    
    return message
