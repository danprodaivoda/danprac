import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))

