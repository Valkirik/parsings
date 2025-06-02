"""import requests
from bs4 import BeautifulSoup



for count in range(1, 7):

    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all('div', class_="w-full rounded border")


    for i in data:
        name = i.find('h4').text.replace("\n", "")
        price = i.find('h5').text.replace("\n", "")
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
        name_price = f"{name}: {price}"

        cards_url = []
        card_url = "https://scrapingclub.com" + i.find("a").get("href")
        cards_url.append(card_url)
        for i in cards_url:
            response = requests.get(i)
            soup = BeautifulSoup(response.text, "html.parser")
            data = soup.find('div', class_="my-8 w-full rounded border")
            description = data.find("p", class_="card-description").text


            print(name_price)
            print(f"image: {url_img}")
            print(description)"""








"""url = "https://scrapingclub.com/exercise/list_basic_detail/90008-E/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


data = soup.find('div', class_="my-8 w-full rounded border")


description = data.find("p", class_="card-description").text
print(description)
"""





