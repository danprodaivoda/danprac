import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))




summ = 0
while True:
    try:
        x = input()
        if x == '':
            break
        summ += int(x)
        print("You summ is:" + str(summ))
    except:
        print("Введите коректные данние")
        print("You summ is:" + str(summ))
print("You summ is:" + str(summ))


