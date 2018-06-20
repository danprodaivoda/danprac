import datetime

def printTimeStamp(name):
 print('prodaivoda yan prodaivoda dan: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))



kPa = int(input("Давление: "))
ft = kPa * 0.981
mmr = kPa * 0.133
ta = kPa * 98.1
print("Давление равно: \n" + str(ft) + " футов на квадратный дюйм \n" + str(mmr) + " милиметров ртутного столба \n" + str(ta) + " атмосфер")

