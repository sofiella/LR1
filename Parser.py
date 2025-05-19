from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omsk.drom.ru/auto/new/all/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    block = soup.find_all('div', limit=20, attrs={'data-ftid': 'bulls-list_bull'})
    return block

if __name__ == '__main__':
    import codecs

    with codecs.open("drom_ads.txt", "w", encoding="utf-8") as f:
        for item in parse():
            title = item.find("h3")
            if title:
                f.write(title.text.strip() + "\n")

    print("Готово! Результаты записаны в drom_ads.txt")