import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


summ = 0
summ_num = 0
try:
    while True:
        num = int(input())
        if num == 0:
            print("Ты ввел 0 и программа закончилась")
            break
        summ += 1
        summ_num += num
except ZeroDivisionError:
    print("Ты ввел 0 первым символом")

print("Среднее значение = " + str(summ_num / summ))




