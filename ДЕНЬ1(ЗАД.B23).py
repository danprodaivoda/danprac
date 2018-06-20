import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

n = int(input())
m = int(input())
d = 0
if n > m:
    d = m
else:
    d = n

while True:
    if n % d == 0 and m % d == 0:
        break
    d -= 1

print("Найбильший спильный дильнык = " + str(d))


