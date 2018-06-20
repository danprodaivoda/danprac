import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

sant = int(input("Сколько ты весишь? "))
du = sant / 2.54
fut = 0
if du <= 12:
    print("ТЫ весишь %.2f дюймов" % du)
else:
    fut = sant//12
    du = sant%12
    print("Ты весишь " + str(fut) + " футов")
    print("i %.2f дюймов" % du)


