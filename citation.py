import requests
from bs4 import BeautifulSoup


URL_QUOTE = "https://citation-celebre.leparisien.fr/citation-du-jour"

url = requests.get(URL_QUOTE)

soup = BeautifulSoup(url.text, 'html.parser')

citation = soup.p.text
auteur = soup.cite.text


def send():
    result = (f"Citation du jour: \n\n"
              f"{auteur} \n"
              f"{citation}\n\n"
              )
    return result


RESULTAT_CITATION = send()

