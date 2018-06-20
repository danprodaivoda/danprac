import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


x = input()
if x == "A+":
    print(">4")
elif x == "A":
    print("4")
elif x == "A-":
    print("3.7")
elif x == "B+":
    print("3.3")
elif x == "B":
    print("3")
elif x == "B-":
    print("2.7")
elif x == "C+":
    print("2.3")
elif x == "C":
    print("2")
elif x == "C-":
    print("1.7")
elif x == "D+":
    print("1.3")
elif x == "D":
    print("1")
elif x == "F":
    print("0")

