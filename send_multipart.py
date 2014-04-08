# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.multipart import MIMEMultipart



# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'email'
msg['From'] = 'ngtthanh1010@gmail.com'
msg['To'] = 'ngtthanh1010@gmail.com'
msg.preamble = 'dfg'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
username = 'ngtthanh1010@gmail.com'
password = 'xxxxxx'
server.login(username,password)

server.sendmail(msg['From'],msg['To'],msg.as_string())
server.quit()
