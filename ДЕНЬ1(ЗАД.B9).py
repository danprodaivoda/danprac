import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


nomer = input("Номер: ")

bukvi = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

if len(nomer) == 6:
    if nomer[0] in bukvi and nomer[1] in bukvi and nomer[2] in bukvi and nomer[3] in num and nomer[4] in num and nomer[5] in num:
        print("Номер правельный")
    else:
        print("Код не правельный")
if len(nomer) == 7:
    if nomer[0] in bukvi and nomer[1] in bukvi and nomer[2] in bukvi and nomer[3] in bukvi and nomer[4] in num and nomer[5] in num and nomer[6] in num:
        print("Номер правельный")
    else:
        print("Код неправельный")



