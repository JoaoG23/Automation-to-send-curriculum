import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "jguilhermeempresarial@outlook.com"
msg["To"] = "joaoguilherme94@live.com"
msg["Subject"] = "Teste Outlook SMTP"
msg.set_content("Enviado com senha de aplicativo.")

with smtplib.SMTP("smtp.office365.com", 587) as smtp:
    smtp.starttls()
    smtp.login("jguilhermeempresarial@outlook.com", "mhnnkpsiklsqxouq")
    smtp.send_message(msg)
    