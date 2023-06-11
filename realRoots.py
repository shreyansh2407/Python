a = int(input("Enter coefficient of x^2:"))
b = int(input("Enter coefficient of x:"))
c = int(input("Enter coefficient of constant:"))
d = (b**2)-4*a*c
if d>0:
    ans1 = (-b+d**1/2)/(2*a)
    ans2= (-b-d**1/2)/(2*a)
    print("Roots are distinct")
    print("Roots are:",ans1,"and",ans2)

elif d==0:
    ans = -b/(2*a)
    print("Roots are equal")
    print("Roots are:",ans,"and",ans)
else:
    print("Roots are not real")
