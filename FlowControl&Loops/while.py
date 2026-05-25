#While Loop

#Print numbers from 1 to 5 using a while loop
count=1

while count<=5:
  print(count)
  count+=1

#Output: 1
#        2
#        3
#        4
#        5

#Calculate the factorial of a number using a while loop
n=5
factorial=1

while n>0:
  factorial*=n
  n-=1

print("Factorial: ",factorial) #Output: Factorial:  120
