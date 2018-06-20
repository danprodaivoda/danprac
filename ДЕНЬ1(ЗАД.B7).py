import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

live = input("Где ты живешь? ")
time = input("Твое временное место жительства? ")
inttime = int(time)
if live == "Будинок":
    if inttime >= 18:
        print("Вєтнамське порося")
    elif inttime < 10:
        print("Змія")
    else:
        print("Собака")
elif live == "Квартира":
    if inttime < 10:
        print("Кішка")
    else:
        print("Хомяк")
elif live == "Гуртожиток":
    if inttime < 6:
        print("Рибки")
    else:
        print("Мурашник")

