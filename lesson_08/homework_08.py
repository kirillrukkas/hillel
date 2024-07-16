# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

def get_sum_of_list_elements(arr: list)->list:
    """Function receives list of strings and converts each element to a list of numbers, if possible.
    Otherwise it displays a message “Не можу це зробити!”

    Args:
        arr (list): input list of strings(for example [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”])
    Returns:
        list: list of sum for each element of input list
    """
    sums = []

    for elem in arr:
        transform_elems = elem.split(",")
        try:
            sum_arr = sum([int(elem) for elem in transform_elems])
        except ValueError as ex:
            print(f"Error: {ex}")
            sum_arr = "Не можу це зробити!"
        sums.append(sum_arr)
    return sums

input_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
print(f"Віхидній масив зі строками: {input_list}")
print(f"Сума чисел масиву: {get_sum_of_list_elements(input_list)}")

input_list = ["dfd1,2,3,4", "1a,2,3,4,50", "1,2,3,a", "10,20,30,40"]
print(f"Віхидній масив зі строками: {input_list}")
print(f"Сума чисел масиву: {get_sum_of_list_elements(input_list)}")
