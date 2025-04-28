import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook  # Import Workbook to create an Excel file

# Step 1: Send a request to the website
url = "https://news.ycombinator.com/news"
response = requests.get(url)  # Fetch the web page content
response.raise_for_status()   # Raise an error if the request failed (e.g., 404, 500)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")  # Parse the page with the built-in HTML parser

# Step 3: Find all article links on the page
links = soup.select(".titleline > a")  # Select all <a> tags inside elements with class "titleline"

# Create two empty lists to store titles and URLs
titles = []
urls = []

# Step 4: Loop through each link found
for link in links:
    title = link.get_text()  # Get the visible text of the link (the article title)
    href = link.get("href")  # Get the URL from the href attribute

    # If the link is a relative URL (does not start with "http"), add the base domain
    if not href.startswith('http'):
        href = 'https://news.ycombinator.com/' + href

    titles.append(title)  # Add the title to the titles list
    urls.append(href)     # Add the full URL to the urls list

    # Print the title and URL to the terminal
    print(title)
    print(href)
    print()  # Print an empty line for better readability

# Step 5: Save the data to a text file
with open("news_links.txt", "w", encoding="utf-8") as txt_file:
    for title, url in zip(titles, urls):
        txt_file.write(title + "\n")  # Write the title
        txt_file.write(url + "\n\n")  # Write the URL and a blank line

# Step 6: Save the data to an Excel file
wb = Workbook()           # Create a new Excel workbook
ws = wb.active            # Get the active worksheet
ws.title = "News Links"    # Set the worksheet title

# Write the header row
ws.append(["Title", "Link"])

# Write the titles and URLs into the worksheet
for title, url in zip(titles, urls):
    ws.append([title, url])  # Write each title and URL as a new row

# Save the workbook
wb.save("news_links.xlsx")  # Save the Excel file with the given name
