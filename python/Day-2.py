# Enter your code here. Read input from STDIN. Print output to STDOUT
mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())
tip = float((mealCost * tipPercent)/100)
tax = float(mealCost * (taxPercent / 100))
totalCost = int(round(mealCost+tip+tax))
print("The total meal cost is %s dollars." % totalCost)
