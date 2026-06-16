from datetime import datetime

prices = [1,5,2,7,2]
avg = 0
for price in prices:
    avg += price
avg = avg / len(prices)

print("MÉDIA DE PREÇOS")
print(avg)
print("=="*50)
print("DIA ALTERADO")

user = {"username": "user",
        "password": "123",
        "last_login": "12-02-26"
        }

dia = datetime.today()
dia_formatado = dia.strftime("%d/%m/%Y")

user.update({"last_login": dia_formatado})
print(user)
print(user["last_login"])

print("=="*50)
print("LISTAS MISTURADAS")
list_1 = ["site.com/a", "a", "site.com/l", "c"]
list_2 = ["site.com/e", "b", "site.com/f", "c"]
list_3 = list_1 + list_2

list_3 = set(list_3)

correct_list = sorted(list_3)
lista = ", ".join(correct_list)
print(lista)