import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


def taxi(metr, price):
   summ = 25 + price * (metr//140)
   return summ

print(taxi(1200, 2))


