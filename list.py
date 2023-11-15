#list
thislist=["apple","banana","cherry"]
for item in thislist:
  print(item)  
list1=["hello","hi","hey"]
list2=["hello","hiii"]
if len(list1)==len(list2):
 print("same")
else:
 print("not")
out=set(list1) & set(list2)
if out:
 print("has")
else:
 print("not")
