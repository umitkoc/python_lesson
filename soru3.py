class Yakala:
    def __init__(self) -> None:
        self.yasakli_kelimeler=["merhaba","köpek","dünya","araba"]
        self.start()
    def start(self):
        kullanici=input("=>")
        for i in self.yasakli_kelimeler:
            kullanici=kullanici.replace(i,len(i)*"*")
        print(kullanici)



if __name__=="__main__":
    Yakala()