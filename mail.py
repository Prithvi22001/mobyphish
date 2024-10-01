import smtplib, ssl
import email.mime.text  # Explicitly import MIMEText

port = 587  # For starttls
smtp_server = "massmail.uconn.edu"
sender_email = "no-reply-mobyphish@uconn.edu"
receiver_email = "amir.herzberg@gmail.com"
password = 'o.fQlX7r-8Yx'

# message = """\
# Subject: Test Mail

# This message is sent from script.Testing script

# Best,
# MobyPhish Team.
# """
import email.mime.multipart
msg = email.mime.multipart.MIMEMultipart()
msg['to'] = receiver_email
msg['from'] = sender_email
msg['subject'] = 'Test Mail'
body='''This message is sent from python.
Testing script.

Best,
MobyPhish Team.
'''
msg.add_header('reply-to', 'mobyphish@uconn.edu')
msg.attach(email.mime.text.MIMEText(body, 'plain'))

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    # server.sendmail(sender_email, receiver_email, message)
    server.sendmail(msg['from'], [msg['to']], msg.as_string())

# server = smtplib.SMTP(MAIL_SERVER)
