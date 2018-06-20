import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



def calc(*args):
    summ = 0
    mass= 0
    calcu = 0
    for i in args:
        for ii in i:
            calcu += ii[1]
            mass += ii[2]
    summ += calcu * 2
    if mass <= 5:
        summ += 10
    elif mass <= 10:
        summ += 12
    elif mass <= 20:
        summ += 15
    else:
        summ += 25
    return summ

print(calc([["som", 10, 5], ["wom", 10, 5], ["tom", 10, 5]]))


