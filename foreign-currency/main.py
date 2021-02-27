import requests
from bs4 import BeautifulSoup
from time import sleep
from os import system


class Foreign:
    def __init__(self):
        super().__init__()
        self.Usd()

    def Usd(self):
        system("cls")
        req = requests.get("https://finans.mynet.com/doviz/usd-dolar/")
        soup = BeautifulSoup(req.content, "html.parser")
        kelime = soup.find_all("div", {"class": "col-3"})
        yuzdelik = kelime[1].text.replace("\n", "")
        alis = kelime[0].text.replace("\n", "")
        satis = kelime[2].text.replace("\n", "")
        durum = float(str(kelime[1].text).replace("\n", "").replace("%", ""))
        if durum < 0:
            system("color c")
        else:
            system("color a")
        print(9*" "+"high"+6*" "+"change"+6*" "+"low")
        print(9 * " " + alis + 6 * " " + yuzdelik + 6 * " " + satis)
        sleep(5)
        self.Usd()

if __name__ == '__main__':
    Foreign()
