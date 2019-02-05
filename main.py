import requests
from bs4 import BeautifulSoup

r = requests.get('https://store.steampowered.com/search/?term=The+witcher')

soup = BeautifulSoup(r.text, 'html.parser')

resultsRow = soup.find_all('a', {'class': 'search_result_row'})

results = []

for resultRow in resultsRow:
    gameURL = resultRow.get('href')
    title = resultRow.find('span', {'class': 'title'}).text
    releaseDate = resultRow.find('div', {'class': 'search_released'}).text
    imgURL = resultRow.select('div.search_capsule img')[0].get('src')
    price = None
    discountedPrice = None
    if (resultRow.select('div.search_price span strike')):
        price = resultRow.select('div.search_price span strike')[
            0].text.strip(' \t\n\r')
        if (resultRow.select('div.search_price')):
            rawDiscountPrice = resultRow.select(
                'div.search_price')[0].text.strip(' \t\n\r')
            discountedPrice = rawDiscountPrice.replace(price, '')

    results.append({
        'gameURL': gameURL,
        'title': title,
        'releaseDate': releaseDate,
        'imgURL': imgURL,
        'price': price,
        'discountedPrice': discountedPrice
    })

print(results)
