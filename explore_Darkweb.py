# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define a function to make a request to a darkweb site
def make_request(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong:", err)

# Define the darkweb site to scrape
darkweb_site = "http://example.onion"

# Make a request to the darkweb site
darkweb_html = make_request(darkweb_site)

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(darkweb_html, 'html.parser')

# Print the title of the page
print(soup.title.string)

# Find all links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
