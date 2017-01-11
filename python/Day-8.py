totalNums = int(input())
phoneBook={}
for i in range(0,totalNums):
    string = input()
    Input = string.split(' ')
    phoneBook[Input[0]]=Input[1]
hell = input()
while hell != "":
    if hell in phoneBook:
        print(hell + "=" + phoneBook[hell])
    else:
        print("Not found")
    hell = input()
