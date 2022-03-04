def is_ascending(a: int, b: int, c: int):
    if a < b < c:
        return True
    else:
        return False

print(is_ascending(10, 12, 8))

def word_concat(a,b):
    result = ""
    if len(a) <= len(b):
        result = a + b
    else:
        result = b + a
    return result

print(word_concat("ecet", "vala"))


