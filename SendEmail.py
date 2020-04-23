# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:18:07 2020

@author: himanshimehta
""" 
import smtplib 
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendingemailuser(rec,state_name):

    subject = "Reply From Covid Bot Regarding Infromation"
    body = "This is an email with attachment sent from CovidBot\n ----------------------------------------------------------------------\n Here are the measures you need to take to keep the virus at bay:\n 1)Avoid close contact with people who are sick. Maintain at least three feet distance between yourself and anyone who is coughing or sneezing.\n 2)Avoid touching your eyes, nose, and mouth.\n 3)Stay home when you are sick.\n 4)Cover your cough or sneeze with a tissue, then dispose of the tissue safely.\n 5)Clean and disinfect frequently-touched objects and surfaces using a regular household \n 6)Wash your hands often with soap and water for at least 20 seconds, especially after going to the bathroom, before eating, and after blowing your nose, coughing, or sneezing.\n 7)If soap and water are not readily available, use an alcohol-based hand sanitiser with at least 60% alcohol. Always wash hands with soap and water when hands are visibly dirty\n ---------------------------------------------------------------------------------- \n Dont go to the cluster quarantine are which is restricted by your locality for more information visit https://www.mohfw.gov.in/"
    sender_email = ""
    receiver_email = rec
    password =""
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    filename = "FAQ.pdf"  # In same directory as script
    
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
