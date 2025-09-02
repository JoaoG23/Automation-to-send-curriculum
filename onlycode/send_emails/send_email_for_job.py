from email.message import EmailMessage
import os
import smtplib
from datetime import datetime
from dotenv import load_dotenv
from send_emails.prepare_to_body_email.prepare_to_body_email import prepare_to_body_email
from send_emails.get_text_from_file.get_text_from_file import get_text_from_file

load_dotenv()
# Configurações para Outlook
HOST_SMTP = os.getenv("HOST_SMTP", "smtp-mail.outlook.com")
PORT_SMTP = int(os.getenv("PORT_SMTP", "587"))
EMAIL_REMETENTE = os.getenv("EMAIL_USER")  
EMAIL_SENHA = os.getenv("APP_PASSWORD") 

def send_email_for_job(job_data):
    """
    Envia email de candidatura para uma vaga
    job_data: lista com [email, tecnologia, descricao_vaga, expectativa_salarial, recrutador, enviado]
    """
    email_destino = job_data[0]
    tecnologia = job_data[1]
    descricao_vaga = job_data[2]
    expectativa_salarial = job_data[3]
    recrutador = job_data[4]
    
    # Preparar o corpo do email usando os templates
    path_templates_body = os.path.join(os.getcwd(), 'onlycode', 'templates')
    corpo_email = prepare_to_body_email(job_data, path_templates_body)
    
    # Adicionar o footer
    path_footer = os.path.join(path_templates_body, "footer.txt")
    footer = get_text_from_file(path_footer)
    corpo_completo = corpo_email + "\n\n" + footer
    
    # Selecionar o currículo baseado na tecnologia
    curriculo_path = selecionar_curriculo_por_tecnologia(tecnologia)
    
    if not curriculo_path:
        print(f"Currículo não encontrado para tecnologia: {tecnologia}")
        return False
    
    # Criar mensagem
    msg = EmailMessage()
    msg['Subject'] = f"Candidatura - {descricao_vaga}"
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = email_destino
    msg.set_content(corpo_completo)
    
    # Anexar o currículo
    try: 
        with open(curriculo_path, 'rb') as f:
            file_data = f.read()
            filename = os.path.basename(curriculo_path) 
            
            msg.add_attachment(
                file_data,
                maintype='application',
                subtype='pdf',
                filename=filename
            )
    except FileNotFoundError:
        print(f"Arquivo de currículo não encontrado: {curriculo_path}")
        return False
    
    # Enviar email
    try:
        with smtplib.SMTP(HOST_SMTP, PORT_SMTP) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_REMETENTE, EMAIL_SENHA)
            smtp.send_message(msg)
            print(f'Email enviado com sucesso para {email_destino} - Vaga: {descricao_vaga}')
            return True
    except Exception as e:
        print(f'Ocorreu um erro ao enviar o e-mail: {e}')
        return False

def selecionar_curriculo_por_tecnologia(tecnologia):
    """
    Seleciona o currículo apropriado baseado na tecnologia da vaga
    """
    path_main = os.path.join(os.getcwd(), 'onlycode', 'resumes')
    curriculos = {  
        'java': os.path.join(path_main, 'joao-guilherme-desenvolvedor-java.pdf'),
        'frontend': os.path.join(path_main, 'joao-guilherme-desenvolvedor-frontend.pdf'),
        'fullstack': os.path.join(path_main, 'joao-guilherme-desenvolvedor-JS-fullstack.pdf'),
        'node': os.path.join(path_main, 'joao-guilherme-desenvolvedor-JS-backend.pdf'),
        'python': os.path.join(path_main, 'joao-guilherme-desenvolvedor-python.pdf'),
        'tecnico_informatica': os.path.join(path_main, 'joao-guilherme-tecnico-em-infomatica.pdf')
    }
    
    # Mapear tecnologias similares
    if tecnologia.lower() in ['java', 'backend']:
        return curriculos['java']
    elif tecnologia.lower() in ['frontend', 'react', 'vue', 'angular']:
        return curriculos['frontend']
    elif tecnologia.lower() in ['fullstack', 'full stack', 'full-stack']:
        return curriculos['fullstack']
    elif tecnologia.lower() in ['node', 'nodejs', 'javascript', 'js']:
        return curriculos['node']
    elif tecnologia.lower() in ['python', 'django', 'flask']:
        return curriculos['python']
    elif tecnologia.lower() in ['tecnico', 'tecnico_informatica', 'suporte']:
        return curriculos['tecnico_informatica']
    else:
        # Padrão para tecnologias não mapeadas
        return curriculos['fullstack']