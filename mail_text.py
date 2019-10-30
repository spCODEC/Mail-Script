# Importing the required libraries

import smtplib
from email.message import EmailMessage

# Add the email-id of all the recipient in the contacts list below
contacts= ['']

msg = EmailMessage()

# Add the subject below ''
msg['Subject'] = ''

# Add the sender's email address below
msg['From'] = ''

msg['To'] = ','.join(contacts)

# Add the the content of the mail below
msg.set_content('')


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

# Here the first argument is for the senders email address
# The second argument is for the password

    smtp.login('SENDER-EMAIL_ADDRESS_HERE','SENDER-MAIL_PASSWORD_HERE')
    smtp.send_message(msg)