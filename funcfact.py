#CO2 PRGRM1
#FACTORIAL OF A NUMBER USING FUNCTION 
def func_fact():
 n=int(input("enter a number"))
 fact=1
 for i in range(1,n+1):
  fact=fact*i
 print(fact)
func_fact()