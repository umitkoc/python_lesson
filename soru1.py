# minimum 5 basamaklı integer girdi sayı ile diziye aktarma ve ters dönüşümü uygulama
class Soru1:
    def __init__(self, sayi):
        self.sayi =sayi
        self.copy=sayi
        self.basamak=self.basamak()
        self.add()
    def add(self):
        self.array=[0]*self.basamak
        i=self.basamak-1
        while i>=0:
            self.array[i]=self.copy%10
            self.copy=int(self.copy/10)
            i-=1
        print(self.array)
        self.reverse()
    def reverse(self):
        i=self.basamak-1
        sayi=0
        while i>=0:
            sayi+=self.array[i]*(10**i)
            i-=1
        print(sayi)
        # recursive
    def basamak(self,i=0):
        if self.sayi<=0.9:
            return i
        else:
            self.sayi =self.sayi/10
            i+=1
            return self.basamak(i)
if __name__ == "__main__":
    Soru1(123456789)
