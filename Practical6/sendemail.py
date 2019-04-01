# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Determine whether the email address  is legal.
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

fpath = r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical6'
fname = 'address_information.csv'
file = fpath + '/' +fname 
tname = 'body.txt'
body= fpath + '/' +tname
infor =  open(file) 
text = open (body)
i = text.read()
for l in infor:
    l=l.rstrip()
    ad = re.findall(r',(\S+@\S+),',l)
#use open() function to open address_information.csv 
    for line in ad:
#get the comma-separated information using regex  re.findall() 
        if re.match (r'\S+@\S+.com',line):
            name = str (re.findall(r'.com,To (\S+):',l))
            name = name[2:-2]
            
            mail_host="smtp.zju.edu.cn"  
            mail_user="3180111431"    
            mail_pass="********"  #not correct password.   
 
            sender = '3180111431@zju.edu.cn'
            receivers = [line]  
 
            passage = re.sub(r'User',name,i)
            message = MIMEText(passage, 'plain', 'utf-8')
            message['From'] = Header("Yuxing", 'utf-8')
            message['To'] =  Header("email", 'utf-8')
 
            subject = re.sub(r'(\S+),','',l)
            message['Subject'] = Header(subject, 'utf-8')
 
            print(line,' :Correct Address! ')
            try:
                smtpObj = smtplib.SMTP() 
                smtpObj.connect(mail_host, 25)    
                smtpObj.login(mail_user,mail_pass)  
                smtpObj.sendmail(sender, receivers, message.as_string())
                print ("Mail sent successfully!")
            except smtplib.SMTPException:
                print ("Error")
            
        else:
            print(line,' :Wrong Address!')
            
# ﬁnd which address is legal and discard the wrong ones  re.match() 
# Send Emails to people who with right email addresses. 


            

 

    