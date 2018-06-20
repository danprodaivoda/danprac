import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

bread = int(input("Сколько вчерашнего хлеба ты хочешь? "))
new_bread = bread * 8.5
print("Если бы ты купил свежий хлеб ты бы заплатил %.2f $" % new_bread)
scidca = new_bread * 0.60
print("Твоя скидка = %.2f $" % scidca)
real_bread = new_bread - scidca
print("Заплати  %.2f $" % real_bread)

