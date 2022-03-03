def is_even(a):
    return a % 2 == 0

print(is_even(8))
print(is_even(11))


def sum_negatives(numbers):
    sum = 0
    for number in numbers:
        if number < 0:
            sum += number
    return sum


print(sum_negatives([-1, 0, 3, 5, -7]))

def to_minutes(hours):
    return hours*60

print(to_minutes(3))

# def input_number(msg):
#     return int(input(msg))
#
# value=input_number("Adj meg egy szamot!")
# print(type(value))



def annotate_every_number(numbers):
    counter = 1
    for number in numbers:
        if is_even(counter):
            print(" " + str(number))
        else:
            print(number)
        counter +=1

annotate_every_number([4, 7, 8, 3, 3])

def concatenate_short(words):
    result = ""
    for word in words:
        if len(word) <= 2:
            result = result + word
    return result

print(concatenate_short(["alma", "ez", "korte", "meggy", "az"]))