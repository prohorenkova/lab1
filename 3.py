y = int(input("Введите год: "))

if y % 4 != 0:
    print(y, " - невисоконый год")

elif y % 100 == 0:
    if y % 400 == 0:
        print(y, " - високоный год")
    else:
        print(y, " - невисоконый год")
else:
    print(y, " - високоный год")
