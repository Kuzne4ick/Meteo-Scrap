from bs4 import BeautifulSoup
import requests
from requests import get


print("""
███╗░░░███╗███████╗████████╗███████╗░█████╗░░██████╗░█████╗░██████╗░░█████╗░██████╗░
████╗░████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║█████╗░░░░░██║░░░█████╗░░██║░░██║╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██║░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░
██║░╚═╝░██║███████╗░░░██║░░░███████╗╚█████╔╝██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░
█████████████████████████
█▄─▄─▀█▄─▄▄─█─▄─▄─██▀▄─██
██─▄─▀██─▄█▀███─████─▀─██
▀▄▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀
""")
input(("""Добро пожаловать в программу MeteoScrap! 
╚═══════════════════════════════════════╝
...
Инструкция:
1. Введите месяц.
~~~~~~~~~~~~~~~~
2. Введите начальную дату анализа
~~~~~~~~~~~~~~~~
3. Введите конечную дату анализа
~~~~~~~~~~~~~~~~

Создатель - @kuzne4ick

Нажмите Enter, чтобы начать... """))

valuesOfTemperature = []
valuesOfPressure = []


def showAverage(numbers):
    new_numbers = []
    for i in range(len(numbers)):
        if numbers[i].find("−") != -1:
            cleanNumber = numbers[i].replace("−", "-")
            new_numbers.append(cleanNumber)
        else:
            new_numbers.append(numbers[i])
    counter = 0
    for i in range(len(new_numbers)):
        counter += int(new_numbers[i])
    return counter/len(new_numbers)


activeMonth = -1
months = ["января", "февраля", "марта", "апреля", "мая", "июня",
          "июля", "августа", "сентября", "октября", "ноября", "декабря"]
month = input("Укажите месяц >> ")
firstDate = input("Введите число , с которого хотите начать анализ >> ")
while firstDate != int():
    firstDate = input("Введите число , с которого хотите начать анализ >> ")
lastDate = int(input("Введите число, каким хотите закончить >> "))
while lastDate != int():
    lastDate = int(input("Введите число, каким хотите закончить >> "))


while activeMonth == -1:
    if month.lower() == "январь":
        activeMonth = 0
        monthUrl = "january"
    elif month.lower() == "февраль":
        activeMonth = 1
        monthUrl = "february"
    elif month.lower() == "март":
        activeMonth = 2
        monthUrl = "march"
    elif month.lower() == "апрель":
        activeMonth = 3
        monthUrl = "april"
    elif month.lower() == "май":
        activeMonth = 4
        monthUrl = "may"
    elif month.lower() == "июнь":
        activeMonth = 5
        monthUrl = "june"
    elif month.lower() == "июль":
        activeMonth = 6
        monthUrl = "july"
    elif month.lower() == "август":
        activeMonth = 7
        monthUrl = "august"
    elif month.lower() == "сентябрь":
        activeMonth = 8
        monthUrl = "september"
    elif month.lower() == "октябрь":
        activeMonth = 9
        monthUrl = "october"
    elif month.lower() == "ноябрь":
        activeMonth = 10
        monthUrl = "november"
    elif month.lower() == "декабрь":
        activeMonth = 11
        monthUrl = "december"
    else:
        activeMonth = -1
        print("Указан неправильный месяц")
        month = input("Укажите месяц >> ")


for i in range(firstDate, lastDate+1):
    url = f"https://weather.rambler.ru/v-moskve/{i}-{monthUrl}/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    if html_soup.find('div', class_="HhSR GyfK"):
        temperature = html_soup.find(
            'div', class_="HhSR GyfK").text.replace("°", "")
    else:
        temperature = html_soup.find(
            'span', class_="Njqa").text.replace("°", "")
    pressure = html_soup.find(
        'div', class_="pressure").text.replace("Давление ", "")
    valuesOfPressure.append(pressure.replace(" мм", ""))
    valuesOfTemperature.append(temperature)
    print(f"""~~~~~~~~~~~~~~~~~~~~~~~~

    Температура {i} {months[activeMonth]}: {temperature}
    Давление {i} {months[activeMonth]}: {pressure}
    """)


print(f"""********---СРЕДНИЕ ЗНАЧЕНИЯ ПО ВЫБРАННЫМ ПРОМЕЖУТКАМ ВРЕМЕНИ---********

        Среднее значение температуры: {round(showAverage(valuesOfTemperature))}
        Среднее значение давления: {round(showAverage(valuesOfPressure))}""")

input("Анализ закончен. Нажмите Enter для выхода.")
