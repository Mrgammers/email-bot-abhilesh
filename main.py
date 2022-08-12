import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('volume', 1)
    engine.setProperty('rate', 200)
def get_info():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('abhileshchavan1234@gmail.com', "#Abhileshrc1@")
    email = EmailMessage()
    email['From'] = 'abhileshchavan1234@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {'abhi': 'abhileshchavan007@gmail.com', 'aryan': 'aryanvaity007@outlook.com',
              'abhilesh': 'chavanabhilesh47@gmail.com',
              'chavan': 'abhileshchavan1234@gmail.com', 'arpit': 'arpeetmakasare123@gmail.com',
              'arun': 'arun.vaity9@gmail.com', 'anita': 'vaity.aryan@fcrit.ac.in',
              'karna': 'aryan.vaity9@icloud.com'}


def get_email_info():
    talk('What is the subject of your email')
    subject = get_info()
    talk('Tell me your text in the email')
    message = get_info()
    talk('To whom you want to send email')
    name = get_info()
    talk("Is this the message you want to send to {} ".format(name))
    print(message)
    talk(message)
    reply = get_info()
    if reply == "yes":
        if 'everyone' in name:
            for receiver in email_list.values():
                print(f"Sending mail to {receiver}")
                send_email(receiver, subject, message)
        else:
            receiver = email_list[name]
            print(f"Sending mail to {receiver}")
            send_email(receiver, subject, message)
        talk('Hey dude. Your email is sent')
        talk('Do you want to send more email?')
        send_more = get_info()
        if 'yes' in send_more:
            get_email_info()
            return
        else:
            return
    else:
        get_email_info()


get_email_info()