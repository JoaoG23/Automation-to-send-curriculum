# Automation to Send Curriculum 📤  

## 1. Introduction  

This project automates the process of sending job application emails, including personalized content and attachments, using Outlook. It extracts data from a CSV file located in the `imports` directory, processes each record, and sends emails efficiently. After successful email delivery, the CSV is moved to the `exported` directory.  

## 2. Technologies Used 📲  

[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-FFD43B?style=for-the-badge&logo=python&logoColor=white)](https://pyautogui.readthedocs.io/)  
[![Python-dotenv](https://img.shields.io/badge/dotenv-150458?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/python-dotenv/)  
[![MouseInfo](https://img.shields.io/badge/MouseInfo-217346?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/MouseInfo/)  
[![Keyboard](https://img.shields.io/badge/Keyboard-0078D4?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/keyboard/)  
[![Pillow](https://img.shields.io/badge/Pillow-FFD43B?style=for-the-badge&logo=python&logoColor=white)](https://python-pillow.org/)  

## 3. Installation 🛠️  

### Steps to install:  

1. Clone this repository:  
   ```bash  
   git clone https://github.com/JoaoG23/automation-to-send-curriculum.git  
   ```  
2. Install the necessary dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Create a `.env` file with the following content:  
   ```env  
    PATH_WHERE_CURRICULUMS="G:\Outros computadores\Meu modelo Laptop\Documents\Curriculos&Apresentações\Curriculos\2024\genericos"
   ```  

## 4. Features ✔️  

- [x] Extract HR email, name, and technologies from a CSV in the `imports` folder.  
- [x] Log in to the company email via Outlook.  
- [x] Compose and send a personalized email:  
    - [x] Add the recipient's email to the **"To"** field.  
    - [x] Write a subject line and introductory message.  
    - [x] Attach the correct resume from the folder.  
- [x] Move the processed CSV file to the `exported` folder after all emails are sent.  

## 5. Directory Structure 📂  

    automation-to-send-curriculum/  
    ├── imports/  
    │   └── data.csv  
    ├── exported/  
    │   └── datetime_sent.csv   
    ├── main.py  
    ├── .env  
    ├── requirements.txt  
    └── README.md  

## 6. How to Use 👨‍💻  

1. Ensure your CSV file is placed in the `imports/` directory and contains the following columns:  
   - Email  
   - HR Name   
   - Technologies  
2. Place the resumes in the `resumes/` folder.  
3. Run the script:  
   ```bash  
   python main.py  
   ```  
4. After execution:  
   - Emails will be sent successfully.  
   - The CSV will be moved to the `exported/` directory.  

## 7. Author  

 <img style="border-radius:50%;" src="https://avatars.githubusercontent.com/u/80895578?v=4" width="100px;" alt=""/>  
 <br />  
 <sub><b>Joao Guilherme</b></sub></a> <a href="https://github.com/JoaoG23/">🚀</a>  

Developed with 🤖 by Joao Guilherme 👋🏽 Contact me via:  

[![Linkedin Badge](https://shields.io/badge/-Joao%20Guilherme-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/joaog123/)](https://www.linkedin.com/in/joaog123/)  
[![Email Badge](https://shields.io/badge/-joaoguilherme94@live.com-c80?style=flat-square&logo=Microsoft&logoColor=white&link=mailto:joaoguilherme94@live.com)](mailto:joaoguilherme94@live.com)  

## 8. License 📄  

[![License](https://shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)  
