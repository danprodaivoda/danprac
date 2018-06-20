import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

summ = int(input("Сколько денег у тебя "))
god1 = summ + summ * 0.14
print("За один час у тебя %.2f $" % god1)
god2 = god1 + god1 * 0.14
print("За 2 часа у тебя %.2f $" % god2)
god3 = god2 + god2 * 0.14
print("За 3 часа у тебя %.2f $" % god3)


