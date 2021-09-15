import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email=EmailMessage()
html=Template(Path('index.html').read_text())
email['from']="Harsh Singh"
email['to']='hgh9harsh@gmail.com'
email['subject']="Succesfull!"

email.set_content(html.substitute({'name':"Harsh"}),"html")

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('wansh619@gmail.com','Wansh#12345')
    smtp.send_message(email)
    print('all good boos!')