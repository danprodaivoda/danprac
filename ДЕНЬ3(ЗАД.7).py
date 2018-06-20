import random
import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

def password():
    passw = ''
    for i in range(random.randint(8,17)):
        passw += chr(random.randint(33, 127))
    print(passw.encode("ascii"))

for i in range(10):
    password()



