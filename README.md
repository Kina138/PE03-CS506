# PE03 - Web Scraping and Working with Spreadsheets

---

## Overview

This program (`new_links.py`) scrapes the latest news articles from [Hacker News](https://news.ycombinator.com/news).  
It collects both the titles and the URLs of the articles, displays them in the terminal, and saves the results into two separate files:
- `news_links.txt` (plain text file)
- `news_links.xlsx` (Excel spreadsheet)

---

## Program Files

- `new_links.py` — Python script that performs the scraping and saves outputs.
- `news_links.txt` — Text file containing the scraped titles and URLs.
- `news_links.xlsx` — Excel file containing the same data in a structured table format.

---

## How the Program Works (Input-Process-Output)

### Input
- The program sends an HTTP GET request to `https://news.ycombinator.com/news` using the `requests` library.
- It retrieves the HTML page content from the website.

### Process
- The program uses the `BeautifulSoup` library to parse the HTML.
- It searches for all `<a>` tags inside elements with the class `titleline` to extract the titles and links.
- If a link is relative (does not start with `http`), it automatically prefixes it with `https://news.ycombinator.com/`.
- The titles and URLs are:
  - Displayed on the screen (terminal output)
  - Saved into a `.txt` file
  - Saved into an `.xlsx` file using the `openpyxl` library.

### Output
- A plain text file `news_links.txt` listing all titles and links.
- An Excel file `news_links.xlsx` with two columns: "Title" and "Link".

---

## Requirements

Before running the program, install the necessary Python libraries:

```bash
pip3 install requests beautifulsoup4 openpyxl
```

---

## How to Run

In the terminal, navigate to the project directory and execute the script:

```bash
python3 new_links.py
```

After running:
- The titles and URLs will appear in the terminal.
- news_links.txt and news_links.xlsx will be generated in the same directory.

---

## Acknowledgments

This project follows the guidelines and materials provided in:
- HOS03 - Web Scraping and Working with Spreadsheets (CS506 Course Material)


