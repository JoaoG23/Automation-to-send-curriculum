import os
import csv
from datetime import datetime
from dotenv import load_dotenv

from send_emails.send_email_for_job import send_email_for_job
from send_emails.update_line_csv_to_email_sended.update_line_csv_to_email_sended import update_line_csv_to_email_sended
from send_emails.verify_email_sent_by_line_csv.verify_email_sent_by_line_csv import verify_email_sent_by_line_csv
from utils.logging.log_manager.log_manager import write_to_log
from utils.move_to_file.move_to_file import move_to_file

load_dotenv()

if __name__ == '__main__':
    try:
        datetime_now = datetime.now().strftime('%Y%m%d%H%M%S')
        
        path_file_imports = os.path.join(os.getcwd(), 'onlycode', 'import', 'jobs.csv')
        path_file_export = os.path.join(os.getcwd(), 'onlycode', 'exported', datetime_now +'.csv')

        # Verificar se o arquivo existe
        if not os.path.exists(path_file_imports):
            print(f"Arquivo não encontrado: {path_file_imports}")
            exit(1)

        with open(path_file_imports, 'r', encoding='utf-8') as file:
            file_read = csv.reader(file, delimiter=';')
            list_file = list(file_read) 
            
            # Remover cabeçalho
            if list_file:
                header = list_file.pop(0)
                print(f"Processando {len(list_file)} vagas...")
            
            emails_enviados = 0
            for i, row in enumerate(list_file):
                print(f"Vaga {i+1}: {row[2] if len(row) > 2 else 'N/A'}")
                
                if not verify_email_sent_by_line_csv(i, path_file_imports):
                    if send_email_for_job(row):
                        if update_line_csv_to_email_sended(i, path_file_imports):
                            emails_enviados += 1
                            print(f"✓ Email enviado e marcado como enviado")
                        else:
                            print(f"✗ Erro ao marcar email como enviado")
                    else:
                        print(f"✗ Falha ao enviar email")
                else:
                    print(f"Email já enviado anteriormente")
        
        print(f"\nProcesso concluído! Emails enviados: {emails_enviados}")
        
        # Mover arquivo processado
        if emails_enviados > 0:
            move_to_file(path_file_imports, path_file_export)
            write_to_log(f'Emails enviados com sucesso! Total: {emails_enviados}')
        
    except Exception as e:
        print(f"Erro: {e}")
        write_to_log(f"Erro: {e}", type='error')