import datetime, random
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
rand = random.randint(34, 37)
if rand == 37:
    rand = "00"
if rand == 0 and rand == "00":
    print("На рулеткі випало " + str(rand) + "\nВиплатити " + str(rand))
else :
    print("На рулеткі випало " + str(rand) + "\nВиплатити " + str(rand))
    if rand != "00":
        if rand in red:
            print("Виплатити Red")
        else:
            print("Виплатити Black")
        if rand != "00" and rand%2 == 0:
            print("Виплатити парне")
        else:
            print("Виплатити непарне")
        if rand != "00" and rand <= 18:
           print("Виплатити 1 - 18")
        else:
            print("Виплатити 19 - 36")



