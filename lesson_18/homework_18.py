

#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

N = 10
# Використання генератора для отримання чисел Фібоначчі
fib = fibonacci_generator()
for _ in range(N):
    print(next(fib))

# Напишіть генератор, який повертає послідовність парних чисел від 0 до N
even_numbers_generator = (x for x in range(N)if x%2==0)

# Використання генератора для отримання парних чисел
for even_number in even_numbers_generator:
    print(even_number)


# Реалізуйте ітератор для зворотного виведення елементів списку.

class MyIterator:
    def __init__(self, list_of_numbers):
        self.current = len(list_of_numbers)+1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            self.current -= 1
            return self.current
        else:
            raise StopIteration

# Використання власного ітератора
my_iterator = MyIterator([1,2,3,4, 5])
for num in my_iterator:
    print(num)

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

I = iter([x for x in range(0,N+1,2)]) # отримат ітератор для списка 
while True:
    try:
        t = next(I) # теж саме що і I.__next__()
    except StopIteration:
        break
    print(t)


# Напишіть декоратор, який логує аргументи та результати викликаної функції.

def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція: {func.__name__}")
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

# Приклад використання
@log_arguments_and_result
def add(a, b):
    return a + b

# Виклик функції
add(3, 5)

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка: {e}")
    return wrapper

# Приклад використання
@handle_exceptions
def divide(a, b):
    return a / b

# Виклик функції з помилкою
divide(10, 0)

# Приклад використання
@handle_exceptions
def get_element_form_list_by_index(a:list, b:int):
    return a[b]

# Виклик функції з помилкою
get_element_form_list_by_index([5,2], 4)