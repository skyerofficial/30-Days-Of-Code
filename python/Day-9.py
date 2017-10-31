# Take Input : Number of which factorial is to be determined 
num = int(input())
# Set Default value of Factorial to be 1
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print(factorial)
