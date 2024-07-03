# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
    ("John", "Doe", 28, "Engineer", "New York"),
    ("Alice", "Smith", 35, "Teacher", "Los Angeles"),
    ("Bob", "Johnson", 45, "Doctor", "Chicago"),
    ("Emily", "Williams", 30, "Artist", "San Francisco"),
    ("Michael", "Brown", 22, "Student", "Seattle"),
    ("Sophia", "Davis", 40, "Lawyer", "Boston"),
    ("David", "Miller", 33, "Software Developer", "Austin"),
    ("Olivia", "Wilson", 27, "Marketing Specialist", "Denver"),
    ("Daniel", "Taylor", 38, "Architect", "Portland"),
    ("Grace", "Moore", 25, "Graphic Designer", "Miami"),
    ("Samuel", "Jones", 50, "Business Consultant", "Atlanta"),
    ("Emma", "Hall", 31, "Chef", "Dallas"),
    ("William", "Clark", 29, "Financial Analyst", "Houston"),
    ("Ava", "White", 42, "Journalist", "San Diego"),
    ("Ethan", "Anderson", 36, "Product Manager", "Phoenix"),
]

def print_list(records: list):
    for record in records:
        print(record)
    print()   

# Task 1 Add your new record o the beginning of the given list
people_records[0:0] = [("Kyrylo", "Rukkas", 55, "Professor", "Lviv")]
print("Add your new record o the beginning of the given list\n")
print_list(people_records)
print("\n-----------\n")

# Tqsk 2  In modified list swap elements with indexes 1 and 5 (1<->5). Print result
print(f"Before: first element: {people_records[1]} fifth element: {people_records[5]}\n")
people_records[1], people_records[5] = people_records[5], people_records[1]
print_list(people_records)
print(f"After: first element: {people_records[1]} fifth element: {people_records[5]}\n")
print("\n-----------\n")

# Task 3 - 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
indexes = [6, 10, 13]
AGE = 30

filtered_list = [
    elem for elem in people_records if (people_records.index(elem) in indexes)
]
filtered_list_by_age = [
    elem for elem in people_records if ((people_records.index(elem) in indexes) and elem[2]>=AGE)
    ]

print(f"List with records indexes {indexes}\n")
print_list(filtered_list)

if filtered_list_by_age:
    print("Records with age >=30 are found\n")
else:
    print("Records with age >= 30 are not found\n")
print_list(filtered_list_by_age)

print("\n-----------\n")
