while(1):
    n = int(input("Enter your number:"))
    if n%5==0 and n%3==0:
        print("Number is divisible by both 3 and 5")
    elif n%5==0:
        print("Number is divisible by just 5")
    elif n%3==0:
        print("Number is divisble by just 3")
    else:
        print("Number is neither  divisible by 3 nor 5")

