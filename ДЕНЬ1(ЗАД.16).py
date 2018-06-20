import datetime
def printTimeStamp(name):
 print('prodaivoda yan prodaivoda dan: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

d = int(input("Долгота поля: "))
sh = int(input("Ширина поля: "))
Sa = d * sh / 100
Sg = d * sh / 10000

print("Площа поля в: \n" + str(Sa) + " Арах\n" + str(Sg) + " Гектарах")

