from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'iamkavi2402@gmail.com'
receiver_email = 'iamkavi2402@gmail.com'
subject = 'Test Email'
message = 'This is a test email.'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Add message body
msg.attach(MIMEText(message, 'plain'))

# Save email content to a text file
with open('text.txt', 'w') as file:
    file.write(f'From: {sender_email}\n')
    file.write(f'To: {receiver_email}\n')
    file.write(f'Subject: {subject}\n')
    file.write('\n')  # Add a blank line to separate headers from the message body
    file.write(message)

print('Email content saved to email_content.txt')
