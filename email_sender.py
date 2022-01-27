# email_sender.py
# Jerrad Flores

# Sends the emails regarding the documentation recorded from the exam.
# Runs after exam ends. 

from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)

def send_email():
    e = input("TEACHER USE ONLY- Please specify teacher email: ")
    return e


def send_message(teacher_email, code):
    sender_email = "testsample0122@gmail.com"
    receiver_email = teacher_email

    msg = MIMEMultipart()
    msg['Subject'] = 'TEST SUBMISSION'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % ("Submission Details: {}".format(code)), 'html')
    msg.attach(msgText)

    msg.attach(MIMEText(open("submission.txt").read()))
    msg.attach(MIMEText(open("mouse.txt").read()))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("testsample0122@gmail.com", "testsample0122#2210")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
        
