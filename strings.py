name = "John Doe"
# print(name.upper())
# print(name[2:6])
# print(name[::-1])
# print("al" in "alma")
# print("b" in "alma")


def char_counting(word):
    count = 0
    for c in word:
        if c == "a":
            count += 1
    return count


print(char_counting("retek"))


def mag_counting(word):
    count = 0
    for c in word:
        if c in "aeiouéíóöőüű":
            count += 1
    return count


print(mag_counting("réparetekmogyoró"))


def star_between_char(word):
    result = ""
    for c in word:
        result += c + "*"
    result = result[0:len(result)-1]
    return result


print(star_between_char("cseresznye"))


def ford(word):
    word2 = word[::-1]
    if word == word2:
        return True
    else:
        return False


print(ford("anna"))


def space_removing(word):
    result = ""
    i = 0
    for c in word:
        if c == " ":
            result = result[0:len(result)]
        else:
            result += c
        i += 1
    return result


print(space_removing("ez ketto space"))

print(name.index("Doe"))
print(name.index("J"))

print("alma korte barack".split())

ip = "192.168.0.1"

print(ip.split("."))
