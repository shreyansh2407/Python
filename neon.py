n = int(input("Enter your number:"))
square  = n**2
result = 0

while(square>0):
    temp = square%10
    result = temp+result
    square = square//10
    


if (n==result):
    print("It is a neon number")
else:
    print("It is not a neon number")
