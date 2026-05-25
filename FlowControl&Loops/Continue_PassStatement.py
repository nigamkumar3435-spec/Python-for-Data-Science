#Continue Statement

#print odd numbers from 1 to 5
for i in range(1,6):
  if i%2==0:
    continue
  print(i)

#Output: 1
#        3
#        5

#Skip negative numbers in a list
numbers=[2,-5,8,-3,10]

for num in numbers:
  if num<0:
    continue
  print("Positive Numbers:",num)

#Output: Positive Numbers: 2
#        Positive Numbers: 8
#        Positive Numbers: 10

#######################################    pass statement    #############################################

#Check if a number is even, do nothing otherwise
num=7

if num%2==0:
  print("Number is even")
else:
  pass
