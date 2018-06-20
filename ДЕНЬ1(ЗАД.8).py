import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

nums = int(input("Введите четырех значный код "))
summ1 = nums//1000
summ2 = nums%1000//100
summ3 = nums%1000%100//10
summ4 = nums%1000%100%10
all_summ = summ1 + summ2 + summ3 + summ4

print("You summ is " + str(all_summ))


