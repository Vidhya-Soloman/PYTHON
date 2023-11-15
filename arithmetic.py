#arithmetic
a=int(input("enter 1st number  "))
b=int(input("enter 2nd number  "))
option=int(input("enter an option  "))
sum=a+b
diff=a-b
prod=a*b
div=a/b
mod=a%b
if option==1:
 print("Sum=",sum)
elif option==2:
 print("Difference=",diff)
elif option==3:
 print("Product=",prod)
elif option==4:
 print("Division=",div)
elif option==5:
 print("Modular=",mod)