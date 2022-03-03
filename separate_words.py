

def conc_words(words):
    result = ""
    i = 0
    for word in words:
        if i == 0:
            result = word
        else:
            result = result + "," + word
        i += 1
    return result

print(conc_words(["a", "b", "c"]))



