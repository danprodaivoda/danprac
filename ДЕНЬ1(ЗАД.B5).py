import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


code = input("Введите 13 значный код: ")

x = int(code[0])*1 + int(code[1]*3) + int(code[2])*1 + int(code[3]*3) + int(code[4])*1 + int(code[5]*3) + int(code[6])*1 + int(code[7]*3) + int(code[8])*1 + int(code[9]*3) + int(code[10])*1 + int(code[11]*3)

tcd = 10 - (x % 10)
if tcd == code[12]:
    print("Ты ввел правельный код")
else:
    print("Твой код не правельный")


