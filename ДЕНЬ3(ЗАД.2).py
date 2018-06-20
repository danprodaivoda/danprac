import random
import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



x = 0
nomera = []
def nomer():
    global nomera
    global x

    nomer1 = '+38(0'
    nomer1 += str(random.randint(0, 9))
    nomer1 += str(random.randint(0, 9))
    nomer1 += ')'
    nomer1 += str(random.randint(0, 9))
    nomer1 += str(random.randint(0, 9))
    nomer1 += str(random.randint(0, 9))
    nomer1 += '-'
    nomer1 += str(random.randint(0, 9))
    nomer1 += str(random.randint(0, 9))
    nomer1 += '-'
    nomer1 += str(random.randint(0, 9))
    nomer1 += str(random.randint(0, 9))
    nomera.append(nomer1)
    x += 1
    if x < 3:
        nomer()

nomer()
print(nomera)




