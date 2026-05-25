# Book Store Web Scraper

A Python web scraping project that extracts book data from the Books to Scrape website using BeautifulSoup and Requests.

## Features
- Scrapes data from multiple pages using pagination
- Extracts:
  - Book Title
  - Price
  - Availability
  - Rating
- Saves data into a CSV file
- Uses Python libraries:
  - requests
  - BeautifulSoup
  - pandas

## Technologies Used
- Python
- BeautifulSoup
- Requests
- Pandas

## Dataset
The scraper collects data from:

:contentReference[oaicite:0]{index=0}

and generates a dataset containing information about books available on the website.

## Output
The extracted data is saved as:

```text
all_books.csv
