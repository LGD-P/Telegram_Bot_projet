import requests
from bs4 import BeautifulSoup


URL = "https://apod.nasa.gov/apod/astropix.html"

url = requests.get(URL)

soup = BeautifulSoup(url.text, 'html.parser')

title = soup.find("b").text

image_end_url_1 = soup.center.find('img')
src = image_end_url_1.get('src')
complete_img_url = URL.replace('astropix.html', src)


def send():
    result = (f"L'image du jour offerte par la NASA est: \n\n"
              f"-{title}:    {complete_img_url} \n\n"
              f"- Lien vers l'article:\n    {URL}\n\n"
              )
    return result


RESULTAT_NASA = send()


###############################################
#             SCHEDULE RESULT
###############################################


"""
schedule.every().day.at("13:03").do(send)


while True:
    schedule.run_pending()
    time.sleep(1)
"""
