no = int(input())
# User Input
for i in range(0,no):
    mainString = input()
    k=0
    evenString = ""
    oddString = ""
    for j in mainString:
        if(k%2):
            oddString += j
        else:
            evenString += j
        k += 1
    print(evenString + " " +oddString)
