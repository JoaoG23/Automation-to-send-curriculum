import random

from send_emails.get_text_from_file.get_text_from_file import get_text_from_file

def prepare_to_body_email(job):
    
    details_job = job[2]
    salary = job[3]
    recruiter = job[4] or 'Recrutador(a)' 
    
    message = ""
    message_random_salary = get_text_from_file("templates/body_with_salary.txt")
    message_salary_replaced = message_random_salary.replace("((details_job))", details_job).replace("((salary))", salary).replace("((recruiter))", recruiter)
    message = message_salary_replaced
    
    if salary == "":
        message_random_without_salary = get_text_from_file("templates/body_without_salary.txt")
        message_without_salary_replaced = message_random_without_salary.replace("((details_job))", details_job).replace("((recruiter))", recruiter)
        message = message_without_salary_replaced
    
    return message
