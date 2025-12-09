# Amazon Price Tracker (Web Scraping + Email Alert)

This project is a simple **price tracker** that monitors a product’s price on a webpage.  
If the price drops below a target amount, the script automatically sends an **email notification**.

The project uses:

- Web scraping (BeautifulSoup4)
- HTTP requests
- Environment variables with `.env`
- SMTP email alerts
- Python automation

---

## 📌 Features

- Scrapes the product title and price from a webpage  
- Converts the scraped price into a float  
- Checks whether the price is below your desired threshold  
- Sends an email alert if the product is on sale  
- Protects sensitive information using a `.env` file  
- Designed to be GitHub-safe (no passwords in repository)

---

## 📂 Project Structure

📦 price-tracker  
┣ 📜 price_tracker.py  
┣ 📜 README.md  
┣ 📜 requirements.txt  
┣ 📜 .gitignore  
┗ 🔒 `.env` (NOT included in GitHub)


