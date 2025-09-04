# Zyczenia urodzinowe
import datetime
from datetime import date

print("Jak masz na imię ? ")
name = input()
print(f"Twoje imie to: {name}" )
print("Podaj date urodzenia w formacie dd.mm.yyyy?")
age_from_input = input()

age_array = list(age_from_input.split("."))

data_urodzenia = date(int(age_array[2]), int(age_array[1]), int(age_array[0]))
print(data_urodzenia)
print(f" Twoja data urodzenia {data_urodzenia}")
today = datetime.date.today()
age = (today - data_urodzenia).days // 365
print(age)


print(f"{name} Wszystkiego najlepszego z okazji urodzin: {age}")








message = "Wszystkiego najlepszego z okazji urodzin"













