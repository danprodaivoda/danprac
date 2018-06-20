import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



def GCD(x, y):
    if x == y:
        return x
    elif x > y:
        return GCD(x - y, y)
    elif x < y:
        return GCD(x, y - x)

print(GCD(135, 20))

