# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 9:

        result = number * multiplier
        # десь тут помила, а може не одна
        if result < 25:            
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
        else:
            break     

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print("---------")


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_elem(a: float, b: float) -> float:
    return a+b

print(sum_two_elem(2,2))
print(sum_two_elem(2.5, 2.7))
print(sum_two_elem(2.5, 2))
print("---------")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
list_of_numbers = [10, 20, 30, 40, 50]
def mean_of_list(arr: list):
    res = 0
    quantity = 0
    for elem in arr:
        res += elem
        quantity += 1
    return res/quantity

print(mean_of_list(list_of_numbers))
print("---------")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
list_of_values = ["hi", "hello", "world", "!"]
def reverse_list(arr:list):
    return arr[::-1]
print(reverse_list(list_of_values))
print("---------")


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
list_of_words = ["hi", "hello", "worlds", "annotations"]
def get_biggest_word(arr:list):
    biggest_word = ""
    for word in arr:
        if len(word)>len(biggest_word):
            biggest_word = word
    return biggest_word
print(f" найдовше слово у списку{ list_of_words} є слово {get_biggest_word(list_of_words)}")
print("---------")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def get_index_of_substring(str1: str, str2: str):
    index = 0

    if str2 in str1:
        c = str2[0]
        for ch in str1:
            if ch == c:
                if str1[index : index + len(str2)] == str2:
                    return index
            index += 1
    return -1

str1 = "Hello, world!"
str2 = "world"
print(get_index_of_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(get_index_of_substring(str1, str2))  # поверне -1
print("---------")
# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

def is_uniq_elem_more_than_ten(arr: list)-> bool:
    """This function return True if quantity of uniq elements more than 10
    else return False

    Args:
        arr (list): List of symbols

    Returns:
        _type_(bool): return True if quantity of uniq elements more than 10
    else return False
    """
    print(f"В строці {len((set(arr)))} унікальних символів ")
    return bool(len((set(arr))) > 10)

my_data = "fdgdfffe43re1298"
print(f"Ця строка має унікальних символи: {set(my_data)} ")

print(f"{is_uniq_elem_more_than_ten(my_data)}")

# task 8
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими

lst1 = ["1", "2", 3, True, "False", 5, "6", 7, 8, "Python", 9, 0, "Lorem Ipsum"]
def get_list_of_string(arr:list)->list[str]:
    """This function create new list which contains only string

    Args:
        arr (list): list which contains different type of elements

    Returns:
        list[str]: list which contains only string
    """
    return [x for x in arr if isinstance(x, str)]
print(f"Початковий спиcок {lst1}")
lst2 = get_list_of_string(lst1)
print(f"Список в якому присутні лише строки із попереднього списку {lst2}")

# task 9
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst1 = [0,1,3,4,5,6,77,88,9]

def get_sum_of_even_numbers(arr: list[int])->int:
    """ get sum of even numbers

    Args:
        arr (list[int]): list of numbers

    Returns:
        int: sum of even numbers
    """

    sum_of_even_numbers = 0
    for item in arr:
        if not item % 2:
            sum_of_even_numbers += item
    return sum_of_even_numbers

print(f"Список чисел: {lst1}")

print(f"Сума усіх ПАРНИХ чисел в цьому ліст дорівнює - {get_sum_of_even_numbers(lst1)}")

# task 10

# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.

car_data = {
    "Mercedes": ("silver", 2019, 1.8, "sedan", 50000),
    "Audi": ("black", 2020, 2.0, "sedan", 55000),
    "BMW": ("white", 2018, 3.0, "suv", 70000),
    "Lexus": ("gray", 2016, 2.5, "coupe", 45000),
    "Toyota": ("blue", 2021, 1.6, "hatchback", 25000),
    "Honda": ("red", 2017, 1.5, "sedan", 30000),
    "Ford": ("green", 2019, 2.3, "suv", 40000),
    "Chevrolet": ("purple", 2020, 1.4, "hatchback", 22000),
    "Nissan": ("pink", 2018, 1.8, "sedan", 35000),
    "Volkswagen": ("brown", 2021, 1.4, "hatchback", 28000),
    "Hyundai": ("gray", 2019, 1.6, "suv", 32000),
    "Kia": ("white", 2020, 2.0, "sedan", 28000),
    "Volvo": ("silver", 2017, 1.8, "suv", 45000),
    "Subaru": ("blue", 2018, 2.5, "wagon", 35000),
    "Mazda": ("red", 2019, 2.5, "sedan", 32000),
    "Porsche": ("black", 2017, 3.0, "coupe", 80000),
    "Jeep": ("green", 2021, 3.0, "suv", 50000),
    "Chrysler": ("gray", 2016, 2.4, "sedan", 22000),
    "Dodge": ("yellow", 2020, 3.6, "suv", 40000),
    "Ferrari": ("red", 2019, 4.0, "coupe", 500000),
    "Lamborghini": ("orange", 2021, 5.0, "coupe", 800000),
    "Maserati": ("blue", 2018, 4.7, "coupe", 100000),
    "Bugatti": ("black", 2020, 8.0, "coupe", 2000000),
    "McLaren": ("yellow", 2017, 4.0, "coupe", 700000),
    "Rolls-Royce": ("white", 2019, 6.8, "sedan", 500000),
    "Bentley": ("gray", 2020, 4.0, "coupe", 300000),
    "Jaguar": ("red", 2016, 2.0, "suv", 40000),
    "Land Rover": ("green", 2018, 3.0, "suv", 60000),
    "Tesla": ("silver", 2020, 0.0, "sedan", 60000),
    "Acura": ("white", 2017, 2.4, "suv", 40000),
    "Cadillac": ("black", 2019, 3.6, "suv", 55000),
    "Infiniti": ("gray", 2018, 2.0, "sedan", 35000),
    "Lincoln": ("white", 2021, 2.0, "suv", 50000),
    "GMC": ("blue", 2016, 1.5, "pickup", 30000),
    "Ram": ("black", 2019, 5.7, "pickup", 40000),
    "Chevy": ("red", 2017, 2.4, "pickup", 35000),
    "Dodge Ram": ("white", 2020, 3.6, "pickup", 45000),
    "Ford F-Series": ("gray", 2021, 3.5, "pickup", 50000),
    "Nissan Titan": ("silver", 2018, 5.6, "pickup", 35000),
}
search_criteria = (2017, 1.6, 36000)


def filter_by_criteria(cars_data: dict, criteria: tuple) -> dict:
    """This function gets cars that satisfy search_criteria.

    Args:
        cars_data (dict): dict of cars data
        criteria (tuple): We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)

    Returns:
        dict: dict of cars that satisfy the criteria 
    """
    year, engine_volume, price = criteria

    return {
        car: (car_color, car_year, car_engine_volume, car_form, car_price)
        for car, (
            (car_color, car_year, car_engine_volume, car_form, car_price)
        ) in cars_data.items()
        if (car_year >= year)
        and (car_engine_volume >= engine_volume)
        and (car_price <= price)
    }

car_data_filter_by_criteria = filter_by_criteria(car_data, search_criteria)
print(
    f"Усього знайдено за крітериямі: рік >= {search_criteria[0]},"
    f" об'єм двигуна >= {search_criteria[1]},  ціна <={search_criteria[2]} - {len(car_data_filter_by_criteria)} машин"
)
for car, params in car_data_filter_by_criteria.items():
    print(car, params)
