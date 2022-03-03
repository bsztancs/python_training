darab=int(input("Hány darab számot szeretnél megadni? "))
sum=0
number=0
for number in range(0,darab):
    number=int(input("Add meg a számot: "))
    if (number>0) and number%2==0:
        sum+=number
print(sum)

