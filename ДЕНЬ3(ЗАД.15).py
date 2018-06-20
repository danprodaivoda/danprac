import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))




arr = [1]
def Catalan(n):
    global arr
    while(len(arr) != n+1):
        arr.append(int(int(arr[len(arr)-1] ) * (4*len(arr)-2)/(len(arr)+1) ) )
    print(arr[n])

Catalan(10)



