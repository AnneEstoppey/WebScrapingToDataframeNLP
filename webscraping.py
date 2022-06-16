from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://www.innovasjonnorge.no/no/tjenester/kundehistorier'
r = requests.get(url)
soup = bs(r.text, 'html.parser')

# print(r.status_code)

# find next level links (all)
links = soup.find_all('a', href=True)
links = [link.get('href') for link in links]
# remove links which do not contain 'kundehistorier'
links = [link for link in links if 'kundehistorier' in link]

# concatenate links with root url
links = ['https://www.innovasjonnorge.no' + link for link in links]
print('Number of links: ', len(links))
# print first 10 links
# print(links[:10])

# one link for testing
# links = ['https://www.innovasjonnorge.no/no/tjenester/kundehistorier/2022/wonderland/']

# scrape description from each link
description = []
for link in links:
    r = requests.get(link)
    soup = bs(r.text, 'html.parser')
    try:
        description.append((link, 
            soup.find('div', class_='rich-text rich-text--lead').text,
            soup.find('div', class_='content-area__block content-area__block-index--0').text, 
            soup.find('div', class_='content-area__block content-area__block-index--2').text))
    except Exception:
        description.append((link, 
            soup.find('div', class_='rich-text rich-text--lead').text,
            soup.find('div', class_='content-area__block content-area__block-index--0').text, ''))

# save text list to csv
df = pd.DataFrame(description)
df.to_csv('description_.csv', index=False, header=False)
