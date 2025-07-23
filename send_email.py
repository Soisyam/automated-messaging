import smtplib
from email.message import EmailMessage

def send_email():
    sender_email = "soyamrai18@gmail.com"
    sender_password = "ggqa kmym yfzm yxgq"
    receiver_email = "soiamrai88@gmail.com"

    subject = "Test Email from Python"
    body = "Hello Soyam! This is a test message sent from Python script."

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    print("Email sent successfully!")

if __name__ == "__main__":
    send_email()
