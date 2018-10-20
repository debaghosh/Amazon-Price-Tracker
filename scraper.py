import requests
from bs4 import BeautifulSoup
import smtplib
from twilio.rest import Client
import time


URL = 'https://www.amazon.in/Six-Crows-Duology-Boxed-Set/dp/1250123569/ref=sr_1_1?keywords=six+of+crows+set&qid=1584291724&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36' }

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content,'lxml')

    title = soup.find(id="productTitle").text
    price = soup.find(id='soldByThirdParty').span.text
    converted_price = float(price.replace("₹","").replace(",",""))
    if(converted_price <= 2500):
        send_mail()
        send_sms()

    print(title)
    print(converted_price)



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    mail_from = 'FROM_EMAIL'
    mail_to = 'TO_EMAIL'
    key = 'KEY'


    server.login(mail_from, key)

    subject = 'Price fell down!'
    body = 'Congratulations! Check the amazon link: '+ URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        mail_from,
        mail_to,
        msg
    )

    print("HEY EMAIL HAS BEEN SENT, DON'T MISS IT!")

    server.quit

def send_sms():
    twilio_phone_number='TWILLIO_NUMBER'
    my_phone_number='MY_NUMBER'
    account_sid = 'ACCOUNT_ID'
    auth_token = 'AUTH_TOKEN'

    client = Client(account_sid, auth_token)
    subject = 'Price fell down!'
    body = 'Congratulations! Check the amazon link: '+ URL
    msg = f"Subject: {subject}\n\n{body}"
    client.messages.create(from_=twilio_phone_number,
                       to=my_phone_number,
                       body=msg)
    print("HEY SMS HAS BEEN SENT!")



check_price()
