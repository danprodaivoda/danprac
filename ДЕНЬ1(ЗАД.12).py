import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

dni = int(input("Сколько дней "))
god = int(input("Сколько часов "))
hv = int(input("Сколько минут "))
sec = int(input("Сколько секунд "))

all_time = dni * 24 * 60 * 60 + god * 60 * 60 + hv * 60 + sec
print("ТЫ путишествовал " + str(all_time) + " секунд")


