year=int(input("Add meg a születési évet: "))
minimum_year=1900
actual_year=2022
if (minimum_year<1900 or actual_year>2022):
    print("Helytelen születési év")
else:
    print("Az életkorod " + str(2022-actual_year) + " év")