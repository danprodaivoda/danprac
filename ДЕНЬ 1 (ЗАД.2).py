import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
zv = int(input("Оберіть одиниці вимірювання:\nякщо в фунтах та дюймах натисніть 1\nякщо в метрах та кілограмах натисніть 2\nВибір: "))

if zv == 2:
    metr = float(input("Метров "))
    kg = int(input("Килограмов "))
    print(kg / (metr ** 2))
elif zv == 1:
    fut = float(input("Футів "))
    dy = float(input("Дюймів "))
    print(703 * dy / (fut ** 2))

