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

def mean_of_list(arr: list)-> float:
    """ Function get mean of list 
    """
    if not arr:
        return "List is empty"
    res = 0
    quantity = 0
    for elem in arr:
        res += elem
        quantity += 1
    return res/quantity

def get_biggest_word(arr:list)->str:
    if not arr:
        return "List is empty"
    biggest_word = ""
    for word in arr:
        if len(word)>len(biggest_word):
            biggest_word = word
    return biggest_word



def get_sum_of_even_list(arr:list)->int:
    if not arr:
        return "List is empty"
    result = 0
    for item in arr:
        if not item % 2:
            result += item
    return result




