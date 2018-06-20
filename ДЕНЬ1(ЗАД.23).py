import datetime
import math
def printTimeStamp(name):
 print('prodaivoda yan prodaivoda dan: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(input("Введіть першу змінну: "))
b = int(input("Введіть другу змінну: "))

s = a + b
r = b - a
d = a * b
ch = a / b
o = a % b
l = b / a
zn = a ** b

print("Сума " + str(s) + "\nРізниця " + str(r) + "\nДобуток " + str(d) + "\nЧастка " + str(ch) + "\nОстача від ділення " + str(o) + "\nЛогарифм " + str(l) + "\nПерша змінна в степені другої " + str(zn))


