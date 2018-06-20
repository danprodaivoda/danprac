import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

storona1 = int(input("1 storona: "))
storona2 = int(input("2 storona: "))
storona3 = int(input("3 storona: "))

if storona1 != storona2 and storona1 != storona3 and storona2 != storona3:
    print("Треугольник не ривносторонный")
elif storona1 == storona2 and storona1 == storona3 and storona2 == storona3:
    print("Треугольник ровносторонный")
else:
    print("Треугольник равнобедренный")
