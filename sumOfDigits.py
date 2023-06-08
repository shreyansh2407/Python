n = int(input("Enter your number:"))
ans = 0
while(n!=0):
    digit = n%10
    ans = ans+ digit
    n = n//10
print(ans)

