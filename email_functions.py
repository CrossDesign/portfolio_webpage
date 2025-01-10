import smtplib, ssl # SSL includes TLS(see below)
import re

""" Use this to send gmail on SMTP via SSL
sender: str, receiver: str, message: str. """


############## EMAIL PROTOCOLS ################
# ABOUT: The main protocols for email handling 
#  Simple Mail Transfer Protocol (SMTP)
#  - SENDING emails and transmission between servers, 
#  Internet Message Access Protocol (IMAP)
#  - SYNCRONIZE emails across multiple devices.
#  Post Office Protocol (POP3)
#  - DOWNLOAD emails to 'one' device 
############## SECURITY ################
# Transport Layer Security (TLS) 
#  - NEW Version of SSL and uses advanced encryption algorithms.
# Secure Sockets Layer (SSL)
# - OLD Version

def validEmail(email):
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    print(valid)
    return valid

def send_email(sender,message,subject='Contact Email'):
    # Set up Transfer Protocol
    host = "smtp.gmail.com"  
    port = 465   # SSL = 465,  TLS = 587
    # app login to email server
    username = "placeholder@gmail.com"
    password = "placeholder app password"
    # sender information
    sender = sender
    receiver = "crosstm08@gmail.com"
    # Message as subject(opt) + message 
    formatted_message = f"""\
Subject: {subject} : {sender}

From: {sender}
Subject: {subject}

{message}
"""
    # generate the Socket Handling object
    ssl_context = ssl.create_default_context()

    try:
        # Call the Protocol with the Socket handler for action
        with smtplib.SMTP_SSL(host=host, port=port, context=ssl_context) as server:
            server.login(user=username,password=password)
            server.sendmail(from_addr=sender,to_addrs=receiver,msg=formatted_message)
    except TypeError:
        print("There was an issue with the email, subject or message.")