n = int(input("Enter your number:"))
ans = 0
temp = n
while(n!=0):
    digit = n%10
    ans = ans + (digit**3)
    n = n//10
if(temp == ans):
    print("Armstrong number")
else:
    print("Not a armstrong number")
