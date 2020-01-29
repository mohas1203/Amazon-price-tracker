import requests
from bs4 import BeautifulSoup 
import smtplib
import time
#Change bottom link to whatever amazon product you want to track
URL = 'https://www.amazon.ca/gp/product/B07KCRTN9Q?pf_rd_p=05326fd5-c43e-4948-99b1-a65b129fdd73&pf_rd_r=AET51YE2ER7XV6XMBRM9'

headers = {"User-Agent": '''search up my user agent and copy paste link here'''}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= "productTitle").get_text()
    price = soup2.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[5:10])

    #Change the "70" in both if statements to what ever price you want the product to go under
    if converted_price < 70:
        send_email()

    print(converted_price)
    print(title.strip())

    if converted_price < 70:
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('''Your email goes here''', '''your passowrd goes here''')

    subject = 'The price fell down!!!'
    #change link on the bottom to whatever price you are trying to track
    body = 'Check the amazon link https://www.amazon.ca/gp/product/B07KCRTN9Q?pf_rd_p=05326fd5-c43e-4948-99b1-a65b129fdd73&pf_rd_r=AET51YE2ER7XV6XMBRM9'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '''Your email again''',
        '''The Email you want to send price to''',
        msg
    )

    print('Email has been sent!')
    server.quit()

while(True):
    check_price()
    time.sleep(60*1440)#chagne this to the amount of times you wnat the program to send an email, (in seconds)