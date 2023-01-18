a=int(input("enter the first year"))
b=int(input("enter the future year"))
while(a<=b):
    if(a%4==0 and a%100!=0 or a%400==0):
       print(a)
    a=a+1 
      
     
  
