# string :
# string is a sequence of characters. It is an immutable data type in Python.
username = "sanjana"

username[0] #s

username[-1] #a

username[0] = "S" #TypeError: 'str' object does not support item assignment

username = "S" + username[1:] #instead of changing the first character, we can create a new string with the desired change

username = username + "!" #adding a character to the end of the string

username = username[:-1] #removing the last character from the string

username = username.upper() #converting the string to uppercase

username = username.lower() #converting the string to lowercase 

username = username.replace("s", "S") #replacing all occurrences of a character in the string


username.replace("s", "S") #replacing all occurrences of a character in the string

username[1:4] #slices the string from index 1 to index 3 (4 is not included)

username[1:4] = "XYZ" #TypeError: 'str' object does not support item assignment

#list :(array in cpp)
# list is a collection of items. It is a mutable data type in Python.

myList = [1, 2, 3, 4, 5]
# methods of list
myList.append(6) #adds an item to the end of the list
myList.index(3) #returns the index of the first occurrence of the item in the list


# dictionary :
# dictionary is a collection of key-value pairs. It is a mutable data type in Python.
myDict = {"name": "sanjana", "age": 20, "city": "New York"} 

# tuple :
# tuple is a collection of items. It is an immutable data type in Python.
myTuple = (1, 2, 3, 4, 5)   
