#Pakages
from email.message import EmailMessage 
import ssl
import smtplib
# SENDER EMAIL & PASSWORDc
email_sender ="iamkavi2402@gmail.com"
email_password="vpdfczueguwwhgmq"
# RECEIVER
email_receiver="iamkavi2402@gmail.com"
# GIVEN ANY WORDS
subject="Hi, I'm your new Full Stack Developer, Kaviarasan.R"
body="""
My name is Kaviyarsan.R, and I have recently joined (company) as the new Full Stack Developer.

I want to introduce myself to you all and take this opportunity to express how excited I am to be joining the company at this point. 

Please feel free to contact me if you would like to get in touch. I'm looking forward to getting to know all of you and working together.

Yours faithfully,
Kaviyarasan.R
"""

# VARIABLE CREATE
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject

em.set_content(body)
context=ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
     smtp.login(email_sender,email_password)
     smtp.sendmail(email_sender,email_receiver,em.as_string())

