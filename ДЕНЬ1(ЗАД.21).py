import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
n = int(input())
c = float(n*(n + 1) / 2)
print (c)
