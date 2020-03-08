# -*- coding: utf-8 -*-
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import csv
import requests
from datetime import date
from bs4 import BeautifulSoup
from config import config
import os 
print(os.getcwd())

def get_price(url):

    headers = {"User-Agent" : config["user_agent"]}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    #title = soup.find(id="productTitle").get_text()
    
    price = float(soup.find(id="priceblock_ourprice").get_text()[1:]) 

    print(price)

    return price

if __name__ == "__main__":
    url = config["url"]
    date = str(date.today())
    data = str(get_price(url))
    
    with open('pricing.csv','a') as csvfile:
        fieldnames = ['Date', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Date': date, 'Price': data})
        csvfile.close()