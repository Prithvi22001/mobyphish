import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
import os
# Email sending function
def send_email(subject, body, recipients):
    port = 587  # For starttls
    smtp_server = "massmail.uconn.edu"
    sender_email =  settings.SENDER_EMAIL
    password = settings.PASSWORD 
    print(f"MAIL SCRIPT user_pass {sender_email},{password} ",flush=True)
    # Create SSL context
    context = ssl.create_default_context()

    try:
        # Establish a connection to the email server
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  
            server.login(sender_email, password)  # Login

            # Send email to each recipient separately
            for recipient in recipients:
                # Create a fresh message for each recipient
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient
                msg['Subject'] = subject
                msg.add_header('reply-to', 'mobyphish@uconn.edu')
                
                # Attach the email body
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                server.sendmail(sender_email, recipient, msg.as_string())
                print(f"Email sent successfully to: {recipient}",flush=True)
            return True
        return "with"

    except Exception as e:
        print(f"Error sending email: {e}",exc_info=True,flush=True)
        return True
    
    return "end"
    


# Example usage:
if __name__ == "__main__":
    subject = "Test Mail"
    body = """\
    This message is sent from a Python script.
    Testing script.

    Best,
    MobyPhish Team.
    """
    recipients = ["recipient1@example.com", "recipient2@example.com"]  # Multiple recipients
    
    # Call the function to send the email separately to each recipient
    send_email(subject, body, recipients)
