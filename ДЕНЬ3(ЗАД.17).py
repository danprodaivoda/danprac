import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))




def rec(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / rec(x, y * -1)
    else:
        if y % 2 == 0:
            return rec(x, y / 2) ** 2
        else:
            return x * rec(x, y - 1)


print(rec(2, 5))

