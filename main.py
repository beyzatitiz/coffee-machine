from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker

print("""Hoş geldiniz, makinemizde aşağıdaki kahveler bulunmaktadır.""")
menü_nesnesi= Menu()
kahveci= CoffeeMaker()
while True:
    print(menü_nesnesi.get_items())

    kahve_ismi= input("Lütfen içmek istediğiniz kahvenin adını yazınız: ")
    kahve= menü_nesnesi.find_drink(kahve_ismi)
    if kahve != None:
        if kahveci.is_resource_sufficient(kahve):
            kahveci.make_coffee(kahve)
        else:
            break
    if kahve_ismi== "report":
        kahveci.report()
    
