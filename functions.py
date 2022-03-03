def print_employee_data(name, age):

    print("Az alkalmazott neve:", name)
    print("Az alkalmazott eletkora:", age)
    # függvény végén a paraméterek törlődnek, nincs többé name és age


def print_dog_name(name):
    print("A kutya neve:", name)


def print_sum(a, b):
    print(a+b)


numbers = [4, 7, 8, 12]

# def sum_list(numbers):
#     result = 0
#     for number in numbers:
#         result += numbers



# sum_list(numbers)


print_sum(3, 4)

print_employee_data("John", 10) #függvény hívás
print_employee_data("Jack", 20)
print_employee_data("Feri", 30)
print_sum(6, 8)
print("End")