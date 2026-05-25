import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
 
# date = input("Enter the date (MM/DD/YYYY): ") 
# page = requests.get(f"https://www.yallakora.com/matches?date={date}#days") 

# def main(page):
#     src= page.content
#     soup = BeautifulSoup(src, 'lxml')
#     print(soup)


# Empty list to store all books
all_books = []

# Loop through pages
for page in range(1, 51):

    # Website URL
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    # Send request
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    # Loop through books
    for book in books:

        # Title
        title = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text

        # Availability
        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        # Rating
        rating = book.p["class"][1]

        # Save data
        all_books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

    print(f"Page {page} scraped successfully!")

# Convert to DataFrame
df = pd.DataFrame(all_books)

# Save to CSV
df.to_csv("all_books.csv", index=False)

print("All data saved successfully!")



