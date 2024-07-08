# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst1 = []

lst1 = [int(item) for item in input("Введіть числа через пробіл: ").split()]

result = 0
for item in lst1:
    if not item % 2:
        result += item

print(f"Список чисел: {lst1}")
print(f"Сума усіх ПАРНИХ чисел в цьому ліст дорівнює - {result}")


