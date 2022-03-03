for i in range(1,11):
    for j in range(1,11):
        print(str(int(i*j)) + " ", end ="")
        if j == 10:
            print("\n")
        j += 1
    i += 1

def digits(numbers):
    for i in str(numbers):
        print(i)

digits(1683)