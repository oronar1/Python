import smtplib
from twilio.rest import Client

TWILIO_SID = "AC26a822665bb0b9a76af184fb044e843e"
TWILIO_AUTH_TOKEN = "ffd97e89489d5d8ee7f7497d40a22e3b"
TWILIO_VIRTUAL_NUMBER = "+12187789366"
TWILIO_VERIFIED_NUMBER = '+972545310514'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com" #YOUR EMAIL PROVIDER SMTP ADDRESS "smtp.gmail.com"
MY_EMAIL = "zeevsemen@gmail.com"
MY_PASSWORD = "kjpxcvbhcxkbused"#Stqr%$dsaf^adgbdcf"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )