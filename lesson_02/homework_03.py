alice_in_wonderland = """
"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where -" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"- so long as I get somewhere," Alice added as an explanation. 
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."""
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print("\n----------------\n")
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
S_black_sea = 436402
S_azov_sea = 37800
S = S_black_sea + S_azov_sea
print(f"Площа обох морів складає = {S} км2")
print("\n----------------\n")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sum_all = 375291
sum_1_2 = 250449
sum_2_3 = 222950
print(f"На першому складі {sum_all-sum_2_3} товарів")
print(f"На другому складі {sum_2_3+sum_1_2-sum_all} товарів")
print(f"На третьому складі {sum_all-sum_1_2} товарів")
print("\n----------------\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
period = 1.5*12
payment = 1179
price = int(period * payment)
print(f"Компютер коштує {price} грівень")
print("\n----------------\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
examples = {8019:8, 9907:9, 2789:5, 7248:6, 7128:5, 19224:9}
for key, value in examples.items():
    print(f"Остача від ділення {key} на {value} дорівнює {key%value}")
print("\n----------------\n")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

list_of_items = {
    "Піца велика":(4, 274),
    "Піца середня":(2, 218),
    "Сік": (4, 35),
    "Торт" :(1, 350),
    "Вода": (3, 21)
}
sum = 0
for key, value in list_of_items.items():
    sum += value[0]*value[1]
print(f"Загальна сума складає {sum} грн")
print("\n----------------\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
max_number = 8  
pages = int(all_photos/max_number)
print(f"Мінімальна кількість сторінок  дорівнює {pages}")
print("\n----------------\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
consumption = 9
capacity = 48
print(f"Для подорожі знадобиться {int(distance/100*consumption)} літрів бензіну")
print(f"Для подорожі знадобиться  заїхаті {int(distance/100*consumption/48)} рази на заправку")
print("\n----------------\n")