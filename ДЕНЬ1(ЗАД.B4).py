import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


hv = int(input("Минут "))
sms = int(input("SMS "))

summ = 15
summ2 = 0

if hv > 200:
    summ += hv - 200 * 0.17
if sms > 50:
    summ += sms - 50 * 0.15

summ2 = summ + summ * 0.05 + 0.44

print("Без комисии ти заплатиш %.2f $" % summ)
print("Ти заплатиш %.2f $" % summ2)


