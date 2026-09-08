from datetime import datetime

fake_base = {}
status = ["новая", "в работе", "выполнена"]

user = str(input("Enter your username: "))
application = str(input("Enter your application: "))

fake_base[user] = {'заявка': application, 'статус': status[0], 'время добавления': datetime.now().strftime("%d.%m.%Y %H:%M")}

print(fake_base)
