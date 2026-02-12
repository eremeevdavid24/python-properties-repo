import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "eremeev11.03.02@gmail.com"
    password = "anea opav bsat lknq"

    receiver = "8zqzfm2ngr@ozsaip.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

send_email("BNS - Biroul National de Statistica!")