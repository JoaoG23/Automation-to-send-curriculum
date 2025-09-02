# (ONLYCODE Version) Automation to Send Curriculum via Email

##### Hours : 8

<img src="./assets/icon.ico" align="right">

## 1. Introduction  

This project automates sending job application emails using SMTP (Gmail), including personalized content and resume attachments. It processes data from a CSV file in the `import` directory, sends emails automatically, and updates the CSV after successful email delivery. This version is lightweight and doesn't require browser automation.

## 2. Technologies Used 📲  

![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![SMTP](https://img.shields.io/badge/SMTP-Email%20Protocol-FF6B6B?logo=gmail&logoColor=white)
![Gmail](https://img.shields.io/badge/Gmail-Email%20Service-EA4335?logo=gmail&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-Comma%20Separated%20Values-FF8800)
![Python](https://img.shields.io/badge/Python-Programming%20Language-3776AB?logo=python&logoColor=white)

## 3. Installation 🛠️  

### Steps to install:  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/JoaoG23/automation-to-send-curriculum.git  
   ```  
2. Navigate to the onlycode directory:
   ```bash
   cd onlycode
   ```
3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
4. Create a `.env` file with the following content:  
   ```env  
   EMAIL_USER=seu_email@gmail.com
   PASSWORD_USER=sua_senha_de_app
   ```  

**Important:** For Gmail, use an App Password, not your regular password. To generate an App Password:
1. Access your Google account
2. Go to Security > Two-step verification
3. App passwords > Generate password for "Email"

## 4. Features ✔️  

- [x] Validate emails already sent.
- [x] Send emails via SMTP (Gmail).
- [x] Compose and send emails:  
    - [x] Add recipient's email.  
    - [x] Write a personalized subject and message.  
    - [x] Attach the correct resume based on job technology.  
- [x] Update the CSV with the sent status.  
- [x] Automatic resume selection based on job requirements.
- [x] Template-based email content with personalization.

## 5. Directory Structure 📂  

    automation-to-send-curriculum/onlycode  
    ├── exported/          # Processed CSV files
    ├── import/            # Input CSV files
    ├── logs/              # Application logs
    ├── resumes/           # Resume PDF files
    ├── send_emails/       # Email sending modules
    ├── templates/         # Email templates
    ├── utils/             # Utility functions
    ├── __init__.py        # Main application
    ├── .env               # Environment variables
    ├── README.md          # This file
    ├── requirements.txt   # Python dependencies

## 6. How to Use 👨‍💻  

1. Place your CSV in the `import/` directory named `jobs.csv`, following this format:

```
Email;Tecnologia;Descricao da vaga;Experctativa Salarial;Recrutador;Enviado
email@empresa.com;java;Desenvolvedor Java;;Nome Recrutador;
```

2. Ensure your resumes are in the `resumes/` directory with the correct naming convention:
   - `joao-guilherme-desenvolvedor-java.pdf`
   - `joao-guilherme-desenvolvedor-frontend.pdf`
   - `joao-guilherme-desenvolvedor-JS-fullstack.pdf`
   - `joao-guilherme-desenvolvedor-JS-backend.pdf`
   - `joao-guilherme-desenvolvedor-python.pdf`
   - `joao-guilherme-tecnico-em-infomatica.pdf`

3. Configure your `.env` file with Gmail credentials.

4. Run the script:  
   ```bash  
   python __init__.py 
   ```  

5. Post-execution:  
   - Emails will be sent automatically.
   - CSV will be updated with the sent status.
   - Processed CSV will be moved to `exported/` folder.

## 7. Requirements  

- Python 3.7+
- Gmail account with App Password enabled
- Stable internet connection

## 8. Benefits and Limitations 🛠️  

### Benefits:  
- Lightweight and fast execution.
- No browser dependencies.
- Reliable email delivery via SMTP.
- Automatic resume selection.
- Template-based personalization.

### Limitations:  
- Requires Gmail account setup.
- Limited to Gmail SMTP (can be extended to other providers).
- Resume files must follow specific naming convention.

## 9. Email Templates  

The application uses customizable templates:
- `body_with_salary.txt` - For jobs with salary information
- `body_without_salary.txt` - For jobs without salary information
- `footer.txt` - Standard signature and contact information

Templates support variables like `((recruiter))`, `((details_job))`, and `((salary))`.

## 10. Author  

 <img style="border-radius:50%;" src="https://avatars.githubusercontent.com/u/80895578?v=4" width="100px;" alt=""/>  
 <br />  
 <sub><b>Joao Guilherme</b></sub></a> <a href="https://github.com/JoaoG23/">🚀</a>  

Developed with 🤖 by Joao Guilherme 👋🏽 Contact me via:  

[![Linkedin Badge](https://shields.io/badge/-Joao%20Guilherme-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/joaog123/)](https://www.linkedin.com/in/joaog123/)  
[![Email Badge](https://shields.io/badge/-joaoguilherme94@live.com-c80?style=flat-square&logo=Microsoft&logoColor=white&link=mailto:joaoguilherme94@live.com)](mailto:joaoguilherme94@live.com)  

## 11. License 📄  

[![License](https://shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)  