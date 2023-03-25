from bs4 import BeautifulSoup
import requests
from requests import get

NORTHERN = "KpFK"
SOUTHERN = "A_Hm"
WESTERN = "oEr2"
EASTERN = "oyjb"
EASTNORTHERN = "EMBA"
EASTSOUTHERN = "ziZF"
WESTSOUTHERN = "_ysh"
WESTNORTHERN = "hpKP"

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
windsNorth = 0
windsSouth = 0
windsNorthEast = 0
windsNorthWest = 0
windsSouthEast = 0
windsSouthWest = 0
windsWest = 0
windsEast = 0


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

firstDate = input("Введите число , с которого хотите начать анализ >> ")
while True:
    try:
        int(firstDate)
    except ValueError:
        firstDate = input(
            "Ошибка! Пожалуйста, введите ЧИСЛО, а не другой тип данных >> ")
    else:
        break
lastDate = input("Введите число, каким хотите закончить >> ")
while True:
    try:
        int(lastDate)
    except ValueError:
        lastDate = input(
            "Ошибка! Пожалуйста, введите ЧИСЛО, а не другой тип данных >> ")
    else:
        break


for i in range(int(firstDate), int(lastDate)+1):
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
    if html_soup.find('svg', class_=NORTHERN):
        windsNorth += 1
        wind = "Северный"
    elif html_soup.find('svg', class_=SOUTHERN):
        windsSouth += 1
        wind = "Южный"
    elif html_soup.find("svg", class_=WESTERN):
        windsWest += 1
        wind = "Западный"
    elif html_soup.find("svg", class_=EASTERN):
        windsEast += 1
        wind = "Восточный"
    elif html_soup.find("svg", class_=WESTNORTHERN):
        windsNorthWest += 1
        wind = "Северо-западный"
    elif html_soup.find("svg", class_=EASTNORTHERN):
        windsNorthEast += 1
        wind = "Северо-Восточный"
    elif html_soup.find("svg", class_=EASTSOUTHERN):
        windsSouthEast += 1
        wind = "Юго-восточный"
    elif html_soup.find("svg", class_=WESTSOUTHERN):
        windsSouthWest += 1
        wind = "Юго-западный"

    valuesOfPressure.append(pressure.replace(" мм", ""))
    valuesOfTemperature.append(temperature)
    print(f"""~~~~~~~~~~~~~~~~~~~~~~~~

    Температура {i} {months[activeMonth]}: {temperature}
    Давление {i} {months[activeMonth]}: {pressure}
    Ветер {i} {months[activeMonth]}: {wind}
    """)


print(f"""ИТОГОВЫЕ ЗНАЧЕНИЯ

        Среднее значение температуры: {round(showAverage(valuesOfTemperature))}
        Среднее значение давления: {round(showAverage(valuesOfPressure))}
        
        Ветра:
        
        Северные - {windsNorth}
        Южные - {windsSouth}
        Западные - {windsWest}
        Восточные - {windsEast}
        Юго-западные - {windsSouthWest}
        Юго-восточные - {windsSouthEast}
        Северо-западные - {windsNorthWest}
        Северо-восточные - {windsNorthEast}
        
        """)

input("Анализ закончен. Нажмите Enter для выхода.")
