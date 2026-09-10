'''
from datetime import datetime

fake_base = {}
status = ["новая", "в работе", "выполнена"]

user = str(input("Enter your username: "))
application = str(input("Enter your application: "))

fake_base[user] = {'заявка': application, 'статус': status[0], 'время добавления': datetime.now().strftime("%d.%m.%Y %H:%M")}

print(fake_base)
'''

from random import randint

category = str(input('Введите категорию заявки: '))
urgency = int(input('Введите приоритет заявки (1-выс/2-норм/3-низк): '))
application_id = randint(1, 1000)

if urgency == 3:
    priority = 'Низкий'
elif urgency == 2:
    priority = 'Нормальный'
else:
    priority = 'Высокий'

print(f"ID заявки: {application_id}\nКатегория: {category}\nПриоритет: {priority}")