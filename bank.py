#Parent Class

class Person():
    def __init__(self,ad,yas,cinsiyet):
        self.ad = ad
        self.yas = yas
        self.cinsiyet = cinsiyet
    
    def detaylariGoster(self):
        print("------------------")
        print("-Kişisel Bilgiler-")
        print("------------------")
        print("Ad:",self.ad)
        print("Yaş:",self.yas)
        print("Cinsiyet:",self.cinsiyet)
        print("----------------")

#Child Class

class Bank(Person):
    def __init__(self, ad, yas, cinsiyet):
        super().__init__(ad, yas, cinsiyet) 
        self.bakiye = 0

    def paraYatir(self,miktar):
        self.miktar = miktar
        self.bakiye = self.bakiye + miktar
        print(self.miktar,"TL para yatırıldı. | Hesabınızdaki bakiye:",self.bakiye,"TL olarak güncellendi.")

    def paraCek(self,miktar):
        self.miktar = miktar
        if self.miktar > self.bakiye:
            print("Yetersiz bakiye. | Hesabınızda",self.bakiye,"TL bulunmaktadır.")
        else:
            self.bakiye = self.bakiye - self.miktar
            print("Hesabınızdan",self.miktar,"TL çekildi. | Kalan bakiye:",self.bakiye)

    def bakiyeSor(self):
        self.detaylariGoster()
        print(f"Sayın {self.ad}. Hesabınızda:",self.bakiye,"TL bulunmaktadır.")









MxAs = Bank("Mehmet", 15, "Erkek")
MxAs.paraYatir(300)
MxAs.paraYatir(422)
MxAs.bakiyeSor()
