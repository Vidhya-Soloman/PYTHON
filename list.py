#CO1 PRGRM 7
#list
l1=[1,2]
l2=[1,3]
#CHECKING FOR SAME LENGTH
if len(l1)==len(l2):
 print("Two list are of same length")
else:
 print("not same length")
#SUM OF TWO LIST
if sum(l1)==sum(l2):
 print("Two list are of same sum",sum(l1))
else:
 print("not same")
#COMMON ELEMENTS
common=set(l1) & set(l2)
if common:
 print("has common",common)
else:
 print("no common")
 