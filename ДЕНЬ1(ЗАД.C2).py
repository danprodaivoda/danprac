import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


x = int(input("Год: "))
y = int(input("Месяц: "))
z = int(input("День: "))
today = datetime.date(x, y, z)
tomorrow = today + datetime.timedelta(days=1)

print("Следуйщий день " + str(tomorrow))

