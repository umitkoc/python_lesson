class Hesaplama:
    def __init__(self, isim1, isim2, vize1, vize2, final1, final2, proje1, proje2, ders):
        ortalama1 = vize1*0.3+final1*0.5+proje1*0.2
        ortalama2 = vize2*0.3+final2*0.5+proje2*0.2
        myList = {
            "ders": ders,
            "isim": (isim1, isim2),
            "vize": (vize1, vize2),
            "final": (final1, final2),
            "proje": (proje1, proje2),
            "ortalama": (ortalama1, ortalama2),
            "durum": (None, None)
        }
        if ortalama1 < ortalama2:
            myList["durum"] = ("kaldı", "geçti")
        else:
            myList["durum"] = ("geçti", "kaldı")
        print(myList)


if __name__ == "__main__":
    Hesaplama("ümit", "mehmet", 45, 40, 35, 85, 80, 50, "ağ programlama")
    Hesaplama("mehmet", "ali", 55, 40, 85, 85, 80, 50, "web tasarım ")
    
