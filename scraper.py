import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
 
all_books = []


for page in range(1, 51):


    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    # Send request
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")


    for book in books:

        title = book.h3.a["title"]


        price = book.find("p", class_="price_color").text


        availability = book.find("p",class_="instock availability").text.strip()

        
        rating = book.p["class"][1]

        
        all_books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

    print(f"Page {page} scraped successfully!")


df = pd.DataFrame(all_books)


df.to_csv("all_books.csv", index=False)

print("All data saved successfully!")



