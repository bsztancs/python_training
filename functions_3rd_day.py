def get_max(a: float, b: float):
    if a > b:
        return a
    if b > a:
        return b
    else:
        return a


print(get_max(4, 4))
print("end of 1st")


def print_square(width: int, height: int):
    full_row = width * "*"
    print(full_row)
    center_row = "*" + (width-2) * " " + "*"
    print((center_row + "\n") * (height - 3) + center_row)
    print(full_row)


print(print_square(6, 6))
print("end of 2nd")


def conc_with_dash(words):
    result = ""
    for word in words:
        result += "-"+word+"-"
    return result


print(conc_with_dash(["alma", "korte", "meggy"]))


