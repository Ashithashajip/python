def sum(a,b):
    "adding two numbers aand b"
    sum=a+b
    return sum

def sub(a,b):
    "substracting two numbers aand b"
    sub=a-b
    return sub

def mul(a,b):
    "multiplying two numbers aand b"
    mul=a*b
    return mul

def div(a,b):
    "dividing two numbers aand b"
    div=a/b
    return div
a1=int(input("enter the first element"))
a2=int(input("enter the second element"))
choice=int(input ("enter the choice 1.addition\2.substracion\3.multiplication\4.division"))
if choice==1:
    print("sum of two numberses :",sum(a1,a2))
elif choice==2:
    print("sub of two numberses :",sub(a1,a2))
elif choice==3:
    print("mul of two numberses :",mul(a1,a2))
elif choice==4:
    print("div of two numberses :",div(a1,a2))
else:
    print("invalid input")
    
    
    


