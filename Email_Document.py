import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Email configuration
sender_email = 'iamkavi2402@gmail.com'
receiver_email = 'iamkavi2402@gmail.com'
subject = 'Test Document Attachment'
message = 'Please find the attached document.'

# SMTP server configuration
####  IT'S NOT WORKING ----- smtp_server = 'smtp.example.com'  ------ #####
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'iamkavi2402@gmail.com'
smtp_password = 'xtvyogmyutqzkrfj'

# Path to the document file you want to attach
document_file_path = 'C:/Users/Kavi/Desktop/EMAIL/transactiondata.csv'

# Create a multipart message with attachment
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEApplication(open(document_file_path, 'rb').read(), Name='transactiondata.csv'))

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email with attachment sent successfully!')
except Exception as e:
    print('An error occurred while sending the email:', str(e))
