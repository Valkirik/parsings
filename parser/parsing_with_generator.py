import requests
from bs4 import BeautifulSoup


def get_list_with_urls():
    for count in range(1, 7): #проходим циклом for по каждой страничке с карточками
        url_1 = f"https://scrapingclub.com/exercise/list_basic/?page={count}" #"count" номер странички
        response_1 = requests.get(url_1)
        soup_1 = BeautifulSoup(response_1.text, "html.parser")
        data_1 = soup_1.find_all('div', class_="w-full rounded border")
        print(data_1)
    #прописав код, что выше, мы получили html страничку с карточками

        for i in data_1:
            url_of_the_card = "https://scrapingclub.com" + i.find("a").get("href")
            yield url_of_the_card

    #на страничке мы получили ссылку на каждую карточку и с помощью генератора вернули эти ссылки


for card_url in get_list_with_urls():
    response_3 = requests.get(card_url)
    soup = BeautifulSoup(response_3.text, "html.parser")
    data = soup.find("div", class_="my-8 w-full rounded border")
    #так же для каждой карточки в каждой страничке получаем html страничку
    
    name = data.find("h3", class_="card-title").text
    price = data.find("h4", class_="my-4 card-price").text
    description = data.find("p", class_="card-description").text
    #вытаскиваем нужную нам информацию

    print(name)
    print(price)
    print(description)









