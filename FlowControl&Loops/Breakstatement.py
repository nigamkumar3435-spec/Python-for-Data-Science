#Break Statement

#find the first even number in a list
numbers=[1,3,58,9,10]

for num in numbers:
  if num%2==0:
    print("First even number found:",num)
    break

#Output: First even number found: 58

#search for a specific element in a list
target_element=42
data=[10,20,30,42,50]

for element in data:
  if element == target_element:
    print("Element found")
    break
#Output: Element found
