import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

chtoto1 = int(input("Сколько штук ты купил "))
chtoto2 = int(input("Сколько штукенций ты купил "))

print("В общем ты будешь нести " + str(chtoto1 * 75 + chtoto2 * 112) + " грам")


