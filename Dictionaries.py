#Dictionaries

#len(dictionary)
my_dict={"fruit":"apple","color":"red","shape":"round"}
my_dict
result=len(my_dict)
print(result)  #Output: 3

#dictionary.keys()
my_dict={"fruit":"apple","color":"red","shape":"round"}
key_list=list(my_dict.keys())
print(key_list)  #Output: ['fruit', 'color', 'shape']

#dictionary.values()
my_dict={"fruit":"apple","color":"red","shape":"round"}
values_list=list(my_dict.values())
print(values_list)  #Output: ['apple', 'red', 'round']

#items
my_dict={"fruit":"apple","color":"red","shape":"round"}
key_list=list(my_dict.items())
print(key_list)  #Output: [('fruit', 'apple'), ('color', 'red'), ('shape', 'round')]

#get
my_dict={"fruit":"apple","color":"red","shape":"round"}
output=my_dict.get("fruit")
print(output)  #Output: apple
output=my_dict.get("size")
print(output)  #Output: None

#pop
my_dict={"fruit":"apple","color":"red","shape":"round"}
removed_color=my_dict.pop("color")
print(removed_color)  #Output: red

removed_color=my_dict.pop("size")
print(removed_color) ### If there is no valid key value pair ,it will throw error

