import requests
from bs4 import BeautifulSoup
import smtplib
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

    print(title)
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('debanjanaghosh123@gmail.com', 'zfvfpthfvrzkansg')

    subject = 'Price fell down!'
    body = 'Check the amazon linkhttps://www.amazon.in/Six-Crows-Duology-Boxed-Set/dp/1250123569/ref=sr_1_1?keywords=six+of+crows+set&qid=1584291724&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'debanjanaghosh123@gmail.com',
        'tanyaghosh240699@gmail.com',
        msg
    )

    print("HEY EMAIL HAS BEEN SENT!")

    server.quit



check_price()
    








