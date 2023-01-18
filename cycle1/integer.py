list1=[1,2,3,4,5,6]
list2=[7,8,3,3]
sum1=0
for i in list1:
    sum1=sum1+i
sum2=0
for i in list2:
    sum2=sum2+i
if len(list1)==len(list2):
    print("length of list are same")
else:
    print("length of list are not same")
if sum1==sum2:
    print("sums of list are equal")
else:
    print("sum of list are not equal")
for i in list1:
    for j in list2:
        if i==j:
            print("common element is",i)