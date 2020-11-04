import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass

error_opening_file = 'File may not exist or error opening file.'

try:
	with open("mail_content.txt") as f_mail_content:
		mail_content = f_mail_content.read()

except Exception:
	print(error_opening_file)

#The mail addresses and password
sender_email_address = input("Enter email address: ")
sender_email_password = getpass.getpass('Enter password: ')

receiver_address = input("Enter reciever email address: ")
subject = input("Enter subject: ")
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_email_address
message['To'] = receiver_address
message['Subject'] = subject

message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = input("Enter file name to attach: ")
attach_file = open(attach_file_name, 'rb') 
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)

payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls() 
session.login(sender_email_address, sender_email_password) 
text = message.as_string()
session.sendmail(sender_email_address, receiver_address, text)
session.quit()
print('Mail Sent')
