import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

latters = ['a', 'e', 'i', 'o', 'u']
user = input("Введите букву ")
if user in latters:
    print("Эта буква голосна")
elif user == 'y':
    print("Эта буква может быть голосна и приголосна")
else:
    print("Эта буква приголосна")

