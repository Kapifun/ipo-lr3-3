day = int(input("Введите день: ")) #запрашивает у пользователя (день) число
month = int(input("Введите месяц: ")) #запрашивает у пользователя (месяц) число
if (month == 3 and day >= 1) or (month == 4) or (month == 5) or (month == 6 and day <= 31):
    season = "Весна" #проверка относится ли дата к весне, если да присваевается переменно 
elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 8 and day <= 31):
    season = "Лето" #проверка относится ли дата к лету, если да присваевается переменно 
elif (month == 9 and day >= 1) or (month == 10) or (month == 11 and day <= 30):
    season = "Осень" #проверка относится ли дата к осени если да присваевается переменно 
else:
    season = "Зима"  #если остальные проверки не проходят условие, season присваевается зима
print(f"Дата {day}.{month} относится к сезону: {season}") #вывод
