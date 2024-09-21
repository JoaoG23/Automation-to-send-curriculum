import os
import csv

from src.utils.send_email_for_job.send_email_for_job import send_email_for_job

if __name__ == '__main__':
    try:
        
        path_imports = os.path.join(os.getcwd(), 'imports', 'jobs.csv')

        with open(path_imports, 'r') as file:
            file_read = csv.reader(file, delimiter=';')
                        
            for row in file_read:
                send_email_for_job(row)
    
    except Exception as e:
        print('Error to run the program: ')