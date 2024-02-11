import smtplib
import datetime as dt
from random import choice

class MailSystem:
    def __init__(self):
        self.your_mail = 'your mail'
        self.password = 'your pass'
        self.address = 'recepient address'
        self.day_of_week = dt.datetime.now().weekday()

    def convert_to_list(self):
        with open('quotes.txt', mode='r') as f:
            self.c = f.readlines()
        self.quotes = list(self.c)
        return self.quotes
    
    
    def send_mail(self):
        self.convert_to_list()
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=self.your_mail, password=self.password)
            connection.sendmail(
                from_addr=self.your_mail, 
                to_addrs=self.address, 
                msg=f'Subject:Monday Quote!\n\n{choice(self.quotes)}')
             
                
m = MailSystem()

day_of_week = dt.datetime.now().weekday()

if day_of_week == 0:
    m.send_mail()
else:
    print('It is not Monday!')