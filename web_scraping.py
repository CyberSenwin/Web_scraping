import pandas as pd
# you must pip install requests
import requests
import ssl
from bs4 import BeautifulSoup

req = requests.get("https://wikipedia.org/wiki/Comparison_of_linux_distributions")

soup = BeautifulSoup(req.content, "html.parser")
print(soup.prettify())

# Or you can try this with jupyter

#It will scrap successful but to see the out put display you have yo use jupyter instead of vscode sir
'''ssl._create_default_https_context = ssl._create_unverified_context

scraper = pd.read_html("https://wikipedia.org/wiki/Comparison_of_linux_distributions")
scraper '''
#beautifulsoup is install