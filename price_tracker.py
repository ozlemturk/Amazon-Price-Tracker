import os
from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

#Get sensitive data from environment variables
#These values MUST NOT be uploaded to Github
SMTP_ADDRESS = os.getenv("smtp_address")
EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

#HTTP request headers to mimic a real browser
header = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding" :"gzip, deflate, br, zstd",
    "Accept-Language" :"tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority" : "u=0, i",
    "Sec-Fetch-Dest" : "document",
    "Sec-Fetch-Mode" : "navigate",
    "Sec-Fetch-Site" : "cross-site",
    "Sec-Fetch-User" : "?1",
    "Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

#Target product page
url = "https://appbrewery.github.io/instant_pot/"

#Send HTTP request
response = requests.get(url, headers={"Accept-Language":"tr-TR"})
html_page = response.text

#Parse HTML page
soup = BeautifulSoup(html_page, "html.parser")

#Extract product price(text sample: "$99")
price = soup.find(name = "span", class_ = "aok-offscreen").getText()

#Remove currency sign and convert to float
price_withot_currency = price.split("$")[1]
price_as_float = float(price_withot_currency)
print("Current Price: ", price_as_float)

#Get product title
title = soup.find(id = "productTitle").get_text().strip()
print(title)

#Your target price threshold
BUY_PRICE = 100

#If the price drops below your desired value, send an email alert
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}"

    #Connect to Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)

        #Send alert email
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs= "ozlemturk2004@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )