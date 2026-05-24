print("Welcome to Python")

#len(list)
my_list=[1,2,3,4,5]
length=len(my_list)
print("Length:",length) #Output: Length: 5

#list.appned(item)
my_list=[1,2,3]
my_list.append(5)
print("New my_list:",my_list) #Output: New my_list: [1, 2, 3, 5]

#list.insert(index,item)
my_list=[1,2,3]
my_list.insert(1,4)
print(my_list)      #Output: [1, 4, 2, 3]

#list.remove(item)
my_list=[1,2,3,4]
my_list.remove(3) #"remove" tells which value to remove
print(my_list)  #Output: [1, 2, 4]

#list.pop(index)
my_list=[1,2,3,4] #"pop" tells what index value is removed
my_list.pop(2)
print(my_list)  #Output: [1, 2, 4]

#list.sort()
my_list=[4,1,3,2]
my_list.sort()
print(my_list)  #Output: [1, 2, 3, 4]

#list.reverse()
my_list=[1,2,3,4]
my_list.reverse()
print(my_list)  #Output: [4, 3, 2, 1]

fruits=["apple","banana","cherry"]
fruits.append("orange")
fruits.insert(1,"mango")
fruits.remove("banana")
fruits.pop(2)
fruits.sort()
fruits.reverse()
print(fruits)         #Output:  ['orange', 'mango', 'apple']
