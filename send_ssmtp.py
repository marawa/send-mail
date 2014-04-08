import smtplib

SERVER = 'smtp.gmail.com:587'
FROM = "ngtthanh1010@gmail.com"
TO = ["ngtthanh1010@gmail.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP(SERVER)
server.starttls()
username = 'xxxx'
password = 'xxxx'
server.login(username,password)
server.sendmail(FROM, TO, message)
server.quit()
