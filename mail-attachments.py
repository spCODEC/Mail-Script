# Importing the required libraries
import smtplib
import imghdr
from email.message import EmailMessage

# Add the email-id of all the recipient in the contacts list below
contacts= ['']

msg = EmailMessage()

# Add the subject below '...'
msg['Subject'] = ''

# Add the sender's email address below
msg['From'] = ''

msg['To'] = ','.join(contacts)

# Add the the content of the mail below
msg.set_content('')

with open('LOCAL-ADDRESS-OF-THE-IMAGE-HERE','rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    # Here the first argument is for the senders email address
    # The second argument is for the password

    smtp.login('SENDERS-EMAIL_ADDRESS_HERE', 'SENDER-MAIL_PASSWORD_HERE')
    smtp.send_message(msg)