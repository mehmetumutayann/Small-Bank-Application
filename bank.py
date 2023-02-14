#Parent Class

class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Kişisel Bilgiler")
        print("")
        print(f"Ad: {self.name}")
        print(f"Yaş: {self.age}")
        print(f"Cinsiyet: {self.gender}")

#Child Class

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender),
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Hesap bakiyesi güncellendi: ", self.balance,"TL")
    
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Yetersiz Bakiye | Hesabınızda: ",self.balance,"TL bulunmaktadır.")
        else:
            self.balance = self.balance - self.amount
            print("Hesabınızdan",self.amount,"TL çekildi | Kalan bakiye: ",self.balance,"TL")

    def bakiyeGoruntule(self):
        print("-----------")
        self.show_details()
        print("Hesabınızda: ",self.balance, "TL bulunmaktadır.")
        print("-----------")




mehmet = Bank("Mehmet Umut",15,"Erkek")
mehmet.deposit(400)
mehmet.deposit(240)
mehmet.bakiyeGoruntule()