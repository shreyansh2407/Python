n = int(input("Enter number of elements you want:"))
a=0
b=1

for i in range(n):
    if i==0:
        print(0)
    elif i==1:
        print(1)
    else:
        next = a+b
        print(next)
        a =b
        b = next
    