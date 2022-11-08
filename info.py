from bs4 import BeautifulSoup
import requests

REFLET_INFO = "https://reflets.info/feeds/public"

request_answer = requests.get(REFLET_INFO)

soup = BeautifulSoup(request_answer.text, "xml")
item = soup.find_all("item")

title_list = [i.title.text for i in item if i.title.text]

link_list = [i.link.text for i in item if i.link.text]


def reflet(titre, lien):
    result = (f"TITRE : {titre[0]}\n\nLIEN: {lien[0]}\n\n"
              f"============================\n\n"
              f"TITRE : {titre[1]}\n\nLIEN: {lien[1]}\n\n"
              f"============================\n\n")
    return result


RESULTAT_REFLET = reflet(title_list, link_list)
