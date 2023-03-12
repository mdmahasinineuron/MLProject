class Customer:

    def __init__(self,name,age,adress) -> None:
        self.name = name
        self.age = age
        self.adress = adress

class Address:

    def __init__(self,city,pincode) -> None:
        self.city = city
        self.pincode = pincode

Cust_1_adress = Address("Bangalore", 560057)

cust1_profile = Customer("Aayan",23,Cust_1_adress)

print(cust1_profile.adress.city)