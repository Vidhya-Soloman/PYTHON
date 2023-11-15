#LIST COMPREHENSION
list1=[1,-2,3,-6,-5,9,10]
num=0
while(num<len(list1)):
 if list1[num]>=0:
  print(list1[num])
 num+=1
#SQUARE
list1=[1,2,3,4,5]
res=[i*i for i in list1]
print(res)
words=["apple","orange","pear","pineapple","strawberry","avocado"]
for word in words:
 if word[0] in "aeiou":
  print(word)
