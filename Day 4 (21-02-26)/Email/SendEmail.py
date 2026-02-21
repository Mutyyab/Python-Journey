import smtplib as smtp
from dotenv import load_dotenv as ld
import os

def send_email(to,from_where,message):

    server = None
    ld('data.env')
    password = os.getenv('PASSWORD')
    try:
        server = smtp.SMTP('smtp.gmail.com', 587)
        # server.set_debuglevel(1)
        server.starttls()
        server.login(from_where, password)
        server.sendmail(from_where, to, message)
        print("Message sent successfully")
    except Exception as e:
        print("Something went wrong:",e)
    finally:
        if server:
            server.quit()