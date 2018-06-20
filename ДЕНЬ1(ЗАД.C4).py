import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


tarif = int(input("Введите какой у вас тариф: "))
mb = int(input("Введите сколько вы потратили мб: "))

if tarif == 5000:
    if mb <= 5000:
        print("Вы имеете 85 грн")
    else:
        print("Вы имеете денег " + str(85 + (mb - 5000) * 0.02) + " грн")
elif tarif == 2000:
    if mb <= 2000:
        print("Вы имеете 35 грн")
    else:
        print("Вы имеете денег " + str(35 + (mb - 2000) * 0.04) + " грн")
        if mb > 5000:
            print("С тарифом 5000мб вы должны оплатить  " + str(85 + (mb - 5000) * 0.02) + " грн")

elif tarif == 1000:
    if mb <= 1000:
        print("Вы имеете 20 грн")
    else:
        print("Вы имеете денег " + str(20 + (mb - 1000) * 0.05) + " грн")
        if mb > 5000:
            print("С тарифом 5000мб вы должны оплатить " + str(85 + (mb - 5000) * 0.02) + " грн")
        if mb > 2000:
            print("С тарифом 2000мб вы должны оплатить " + str(35 + (mb - 2000) * 0.04) + " грн")

