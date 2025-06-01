import requests
from bs4 import BeautifulSoup
from time import sleep

for count in range(1, 7):

    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
    response = requests.get(url) #запрос на сайт для получения html страницы
    soup = BeautifulSoup(response.text, "html.parser") #данной командой получаем читабельный вид
    data = soup.find_all('div', class_="w-full rounded border") #находим нужный участок кода, который будем разбирать(получая список всех карт)


    for i in data: #проходим цыклом беря каждую отдельную карточку
        name = i.find('h4').text.replace("\n", "") #вытаскиваем имя
        price = i.find('h5').text.replace("\n", "") #вытаскиваем цену
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src") #вытаскиваем кортинку
        name_price = f"{name}: {price}" #преобразуем в читабельную строку для дальнейшего вывода

        cards_url = [] #создаем пустой список куда будем закидывать ссылку внутрь каждой карточки, чтобы получить больше информации
        card_url = "https://scrapingclub.com" + i.find("a").get("href") #получаем ссылку на каждую карточку
        cards_url.append(card_url) #закидываем в пустой список
        for i in cards_url: #проходим по каждой карточке
            response = requests.get(i) #запрос на получение html странички каждой карточки
            soup = BeautifulSoup(response.text, "html.parser") #преобразование в читабельный вид
            data = soup.find('div', class_="my-8 w-full rounded border") #находим нужный участок кода для дальнейшей работы
            description = data.find("p", class_="card-description").text #вытаскиваем описание

            #дальше все просто вывоим в консоль
            print(name_price)
            print(f"image: {url_img}")
            print(description)