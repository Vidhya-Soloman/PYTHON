#print sum of 1st 100 even number
n= int(input(" Please Enter the Maximum Value : "))
sum= 0
i= 1
while i<=n:
    if(i % 2 == 0):
     print(i)
     sum=sum+i
    i=i+1
print("The Sum of Even Numbers is",sum)