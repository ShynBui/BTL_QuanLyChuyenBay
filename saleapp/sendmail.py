from email.message import EmailMessage
import ssl
import smtplib


def send(receiver, email_receiver, otp):
    email = 'openunited.hotel@gmail.com'
    password = "woefzmxjarmmyuaa"
    subject = "Xác nhận tài khoản"

    body = """

    Xin chào {},
    Đây là mã xác nhận của bạn: {}

    """.format(receiver, otp)

    em = EmailMessage()
    em['From'] = email
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, email_receiver, em.as_string())

