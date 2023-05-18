from datetime import date
import smtplib
#import schedule
import time
import requests
from bs4 import BeautifulSoup
from username_password import username, password

def send_email():
    smtp_object = smtplib.SMTP('smtp.gmail.com',587)
    smtp_object.ehlo()
    smtp_object.starttls()

    def quote():
        res = requests.get("https://www.brainyquote.com/quote_of_the_day")
        soup = BeautifulSoup(res.text,"html.parser")
        qod = soup.find("a",{"class":"b-qt qt_149960 oncl_q"})
        the_quote = " ".join([x for x in qod.text.split("\n") if x != ""])
        return the_quote
    def author():
        res = requests.get("https://www.brainyquote.com/quote_of_the_day")
        soup = BeautifulSoup(res.text,"html.parser")
        aod = soup.find("a",{"class":"bq-aut qa_149960 oncl_a"})
        the_author = " ".join([x for x in aod.text.split("\n") if x != ""])
        return the_author
    def link(author_name):
        res = requests.get("https://www.brainyquote.com/quote_of_the_day")
        soup = BeautifulSoup(res.text,"html.parser")
        url = "https://en.wikipedia.org/wiki/"
        author_list = author_name.split(" ")
        author_name = author_list[0] + "_" + author_list[1]
        return url + author_name

    email = username()
    mypassword = password()
    smtp_object.login(email,mypassword)
    myquote = quote()
    myauthor = author()
    webpage = link(myauthor)

    from_address = ""
    to_address = ""
    subject = "Quote of The Day"
    message = myquote + " - " + myauthor + "\n" + webpage
    msg = "Subject: " + subject + '\n' + message
    smtp_object.sendmail(from_address,to_address,msg)

#schedule.every().day.at('11:36').do(send_email)

#while True:
#    schedule.run_pending()
#    time.sleep(1)
send_email()
