import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

baks = int(input("Ваша сдача: "))
nominals = [2,1,5,10,50]

nominals.sort()
nominals.reverse()
summ = 0
print (baks, '$ =>')

for k in nominals:
    d = baks//k
    baks = baks -d*k
    print (k,'$ :',int(d))
    summ += d

print ('В сумме:', summ)


