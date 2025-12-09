import os

from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv

#.env dosyasını yüklemek
load_dotenv()

#.env'den bilgileri almak
SMTP_ADDRESS = os.getenv("smtp_address")
EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

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


url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(url, headers={"Accept-Language":"tr-TR"})
html_page = response.text

soup = BeautifulSoup(html_page, "html.parser")
print(soup.prettify())

price = soup.find(class_ = "a-offscreen")
price_without_currency = price.getText().split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id = "productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price.get_text()}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)

        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs= "ozlemturk2004@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
