import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan : ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

x = float(input("Введите амплитуду "))
if 0< x < 2.0:
    print("micro")
elif 2.0 <= x < 3.0:
    print("very minor")
elif 3.0 <= x < 4.0:
    print("minor")
elif 4.0 <= x < 5.0:
    print("light")
elif 5.0 <= x < 6.0:
    print("moderate")
elif 6.0 <= x < 7.0:
    print("strong")
elif 7.0 <= x < 8.0:
    print("major")
elif 8.0 <= x < 10.0:
    print("great")
else:
    print("meteoric")




