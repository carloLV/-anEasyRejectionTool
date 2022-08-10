# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Spyder Editor

This is a temporary script file.
"""

# Import smtplib for the actual sending function
import smtplib
import chime
from tkinter import *
from email.message import EmailMessage

chime.theme('zelda')

def gmail_login(user,pwd,msg):
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo() # optional, called by login()
    server_ssl.login(user, pwd)  
    server_ssl.send_message(msg)
    server_ssl.close()
    
def generic_login(user,pwd,msg):
    server = smtplib.SMTP("Altro server")
    ## server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()

def send_email(recipient, name):
    with open("authentication.txt") as f:
        lines = [line for line in f]
        
    user = lines[0] 
    pwd = lines[1]
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = 'Interview result - hahaha'

    # Prepare actual message
    message = """
    Dear %s,\n
    We are sorry to inform you that you were not selected.
    Go ask somebody else to hire somebody with so poor skills.
    
    Best regards
    """ % (name)
    # Prepare actual message
    # message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    # """ % (user, ", ".join(TO), SUBJECT, name)
    
    ## Create email type message
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Interview result - hahaha'
    msg['From'] = user
    msg['To'] = TO[0]
    
    try:
        ### GMAIL Server
        gmail_login(user,pwd,msg)
        print ('successfully sent the mail')
        chime.success()
    except Exception as e:
        try:
            generic_login(user, pwd, msg)
            print ('successfully sent the mail')
            chime.success()
        except Exception as e:
            chime.error()
            print ("failed to send mail")
            raise e
        chime.error()
        
main = Tk()
main.title("An Easy Rejection Tool, AERT")
main.geometry("1000x500")
width = 1000
height = 1000

def submit():  # Callback function for SUBMIT Button
    text = textbox.get("1.0", END)  # For line 1, col 0 to end.
    t = text.split(",")
    email = t[0]
    name = t[1]
    send_email(email, name)
    print(f'{text=!r}')

def quit():
    chime.info()
    main.destroy()

c = Canvas(main, width=width, height=height, highlightthickness=0)
c.pack()

submitbutton = Button(c, width=30, height=2, text='REJECT THIS MOFO', command=submit)
submitbutton.pack()

textbox = Text(c, width=30, height=2)
textbox.pack()

tboxlabel = Label(c, text='Write email,name\n like yourmama@hotmail.com,mama')
tboxlabel.pack()

quitbutton = Button(c, width=10, height=1, text='QUIT', command=quit)
quitbutton.pack()

mainloop()

authentication.txt