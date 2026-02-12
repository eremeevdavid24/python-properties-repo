import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "eremeev11.03.02@gmail.com"
    sender_password = "anea opav bsat lknq"

    receivers = [
        "8zqzfm2ngr@ozsaip.com",
        "cd6hq@dollicons.com",
        "jwftlo_cz@mediaeast.uk"

    ]

    subject = "Salut Sorin! Esti un super eroi."
    body = "Mesaj"

    for receiver_email in receivers:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email trimis către {receiver_email}")
        except Exception as e:
            print(f"Eroare la trimiterea către {receiver_email}: {e}")

if __name__ == "__main__":
    send_email()