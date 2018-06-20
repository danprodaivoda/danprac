import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

time = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]

papu = input("+ если попугай говорит, я хочу спать")
my_time = int(input("A сколько времени? "))
if papu == '-':
    print("Если попугай молчит не тормоши его")
elif papu == '+' and my_time not in time:
    print("Сейчас день я сплю не трогая меня")
else:
    print("Накрой простынёй клетку попугая")


