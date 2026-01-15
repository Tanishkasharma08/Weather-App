#HELLO WORLD PROGRAM
#print("HELLO, WORLD!")

#VARIABLE DECRALATION PROGRAM
"""name = "Belly"
age = "22"
print("My name is", name)
print("My age is", age)"""

#ASSIGNMENT OPERATOR
"""name = "Belly"
age = "25"
new_age = age
print("My age is", new_age)"""

#Getting the Type of Variable
"""name = "Belly"
age = 22
marks = 88.55
print(name, "->", type(name))
print(age, "->", type(age))
print(marks, "->", type(marks))"""

#Type Casting
"""num_1 = 12    
num_2 = 3.6
res = num_1 + num_2 
print(res, "=>", type(res))"""  

#Implicit Type Casting
"""a = 5 
b = 7.6
c = 3 + 4j   
d = a + b   
e = a + b + c 
print("result1 : ",d, '=>', type(d))   
print("result2 : ",e, '=>', type(e))"""

#Taking input from user and printing it
"""name = input("name : ")
print(name)"""

#if statement
"""x = int(input("Enter the value : "))
y = int(input("Enter the value : "))
if x > y:
    print("Yes, x is greater than y ")"""

#if-else statement
"""x = int(input("Enter the value : "))
if x%2==0:
    print("Yes, x is even ")
else:
    print("Yes, x is odd ")"""

#elif statement
"""a = int(input("Enter the value:  "))
b = int(input("Enter the value:  "))
x = input(" Enter the operator(+, -, *, /)")
if x == '+':
    c = a + b
    print("Addition : ", c)
elif x == '-':
    c = a - b
    print("Subtraction : ", c)
elif x == '*':
    c = a * b
    print("Multiplication : ", c)
elif x == '/':
    c = a / b
    print("Division : ", c)
else:
    print(" You enter wrong operator ")"""

#nested statement
"""a = int(input("Enter the value : "))
b = int(input("Enter the value : "))
c = int(input("Enter the value : "))
if a > b:
    if a > c:
        print(" a is greatest ")
    else:
        print(" c is greatest ")
else:
    if b > c:
        print(" b is greatest ")
    else:
        print(" c is greatest ")"""

#for loop
"""x = int(input("Enter the value"))
n = x
a = 0
b = 1
print(a)
print(b)
for x in range(n):
    c = a + b
    print(c)
    a = b
    b = c"""

#nested-for loop
"""n = 5
for i in range(n+1):
    for j in range(1, i+1):
        print(end = " * ")
    print()"""

#while infinite loop
"""a = int(input("Enter the value"))
z = a
b = 0
while(a>0):
    c = a%10
    x = c**3
    a = a//10
    b = b+x
if b==z:
    print("This is Armstrong Number")
else:
    print("This is not an Armstrong Number")"""

#while finite loop
"""a = int(input("Enter the value : "))
x = 1
i = 1
while(i<a+1):
    x = x*i
    i=i+1
    print(" Fatorial : ", x)"""

#pass statement
"""for i in range(10):  
    if i == 5:  
        pass  
    else:  
        print(i)"""

#continue statement
"""for num in range(1, 11):  
    if num % 2 == 0:  
        continue 
    print(num)"""

#break statement
"""i = 1
while(i>0):
    x = int(input(" Enter the value : "))
    y = int(input(" Enter the value : "))
    z = x + y
    print(z)
    print(" Do you want to continue press 1 or exit press any key ")
    cn = int(input())
    if cn!=1:
        break"""

#String
"""sample_string = "tpointtech"     
print("String:", sample_string)  
print("Data Type:", type(sample_string))"""  

#String Slicing
"""s = "Tpoint Tech"  
print("Given String:", s)    
print("s[1:5] =", s[1:5])   
print("s[:4] =", s[:4])   
print("s[4:] =", s[4:])"""
  
#Creating a String 
"""str_1 = 'Welcome to Tpoint Tech'  
print("String 1:", str_1)  
str_2 = "Welcome to Tpoint Tech"  
print("String 2:", str_2)"""  

#Accessing String with Positive Indexing
"""s = "Tpoint Tech"  
print("Given String:", s)   
print("s[4] =", s[4])  
print("s[9] =", s[9])"""  

#Accessing String with Negative Indexing
"""s = "Tpoint Tech"  
print("Given String:", s)  
print("s[-1] =", s[-1])  
print("s[-6] =", s[-6])"""  

#Deleting a String
"""msg = "tpointtech"   
del msg  
print(msg)"""  

#Updating a String
"""given_str = "welcome learners"  
print("Given String:", given_str)   
new_str_1 = "W" + given_str[1:]    
print("New String :", new_str_1)""" 
 
#String Concatenation
"""str_1 = "Tpoint"  
str_2 = "Tech"  
str_3 = str_1 + " " + str_2  
print("Concatenated String:", str_3)"""
 
#String Repetition
"""str_1 = "Tpoint" 
str_2 = str_1 * 4  
print("Repeated String:", str_2)"""

#String Membership Test
"""given_str = 'Tpoint Tech'   
print("Does 'p' exist in '{given_str}'?", 'p' in given_str)  
print("Does 'a' exist in '{given_str}'?", 'a' in given_str)  
print("Does 'e' not exist in '{given_str}'?", 'e' not in given_str)  
print("Does 'g' not exist in '{given_str}'?", 'g' not in given_str)"""  

#len()
"""given_str = "tpointtech"  
print("Given String:", given_str)  
num_of_chars = len(given_str)  
print("Number of Characters:", num_of_chars)"""

#replace()
"""str_1 = "Learning Python with TpointTech is fun!"  
print("String 1:", str_1)  
print("After replacing 'fun' with 'amazing':")  
print(str_1.replace("fun", "amazing"))"""

#String Methods to Change Case
"""str_1 = str.upper("i love learning python")   # using upper() method  
str_2 = str.lower("PYTHON IS FUN WITH TPOINT TECH") # using lower() method  
str_3 = str.title("welcome to tpoint tech")   # using title() method  
str_4 = str.capitalize("welcome to tpoint tech")  # using capitalize() method  
str_5 = str.swapcase("Learning Python Feels Wonderful")  # using swapcase() method   
print(str_1)  
print(str_2)  
print(str_3)  
print(str_4)  
print(str_5)"""  

#List
"""Li = [20, 'TpointTech', 35.75, [20, 40, 60]]  
print(Li)"""

#List Slicing
"""li = [1, 10, 15, 20, 17, 19]
for i in range(2,5):
    print(li[i])"""

#Creating a list
"""a = [11, 4, 23, 71, 58]  
b = [1, "Hello", 6.74, True]   
print(a)  
print(b)"""

#Find the length of a list
"""li = [1, 5, 7, 10, 15, 20, 11, 55]
print(len(li))"""

#Finding the Largest Number in a List
"""a = [1, 6 , 9, 10, 15, 55]
print(max(a))"""

#Finding the Smallest Number in a List
"""a = [1, 6 , 9, 10, 15, 55]
print(min(a))"""

#Calculating Sum of Elements in a List
"""l1 = [1, 5, 7, 9, 10]
print("Sum of elements in a list : ", sum(l1))"""

#Accessing List Elements
"""li = [15, 23, 47, 32, 94]  
print(li[2])    
print(li[-4])"""

#Updating Elements into a List
"""li = [1, 23, 55, 76]
li[2]=45
print(li)"""

#Iterating Over Lists
"""li = [1, 10, 15, 17, 25, 30]
for i in li:
    print(i)"""

#Append List
"""list_of_fruits = ['apple', 'mango', 'banana', 'orange', 'guava']   
print("List of Fruits:", list_of_fruits)   
list_of_fruits.append('grapes')   
print("Updated List of Fruits:", list_of_fruits)"""

#Extend List
"""shopping_list = ['milk', 'bread', 'butter']  
new_items = ['eggs', 'apples', 'coffee']  
print("Old Shopping List:", shopping_list)  
print("New Items:", new_items)  
shopping_list.extend(new_items)   
print("Updated Shopping List:", shopping_list)"""

#Insert List
"""shopping_list = ['milk', 'bread', 'butter', 'coffee']   
print("Old Shopping List:", shopping_list)   
shopping_list.insert(2, 'eggs')  
print("New Shopping List:", shopping_list)"""

#Remove List
"""a = [1, 5, 7, 9 ,11 ,13]
print("Old List : ", a)
a.remove(9)
print("New List : ",a)"""

#Pop List
"""shopping_list = ['milk', 'bread', 'eggs', 'butter', 'coffee']   
print("Old Shopping List:", shopping_list)  
popped_item = shopping_list.pop(1)    
print("New Shopping List:", shopping_list)  
print("Popped Item:", popped_item)"""

#Clear List
"""shopping_list = ['milk', 'bread', 'eggs', 'butter', 'coffee']   
print("Old Shopping List:", shopping_list)   
shopping_list.clear()    
print("New Shopping List:", shopping_list)"""  

#Index List
"""shopping_list = ['milk', 'bread', 'eggs', 'butter', 'coffee']    
print("Shopping List:", shopping_list)   
item_index = shopping_list.index('butter')   
print("Index of butter:", item_index)"""  

#Count List
"""shopping_list = ['milk', 'bread', 'egg', 'milk', 'butter', 'coffee', 'egg', 'flour', 'egg']    
print("Shopping List:", shopping_list)    
item_count = shopping_list.count('egg')  
print("No. of Eggs:", item_count)"""

#Sort List
"""fruit_basket = ['mango', 'apple', 'orange', 'banana', 'grapes']    
print("Unsorted Fruit Basket:", fruit_basket)    
fruit_basket.sort()   
print("Sorted Fruit Basket:", fruit_basket)"""

#Reverse List
"""fruit_basket = ['apple', 'banana', 'grapes', 'mango', 'orange']   
print("Fruit Basket:", fruit_basket)  
fruit_basket.reverse()   
print("Reversed Fruit Basket:", fruit_basket)"""  

#Copy List
"""fruit_basket = ['apple', 'banana', 'grapes', 'mango', 'orange']    
print("Fruit Basket:", fruit_basket)    
new_fruit_basket = fruit_basket.copy()    
print("Copied Fruit Basket:", new_fruit_basket)"""  

#Tuple
"""T = (20, 'Tpointtech', 35.75, [20, 40, 60])  
print(T)"""  

#Slicing Tuple
"""a = (1, 10, 12, 15, 17, 20, 25)
print(a[1:-1])"""

#Creating a Tuple
"""int_tpl = (13, 56, 27, 18, 11, 23)  
print("Tuple with integers: ", int_tpl)        
mix_tpl = (6, "Tpointtech", 17.43)      
print("Tuple with different data types: ", mix_tpl)"""  

#Accessing Tuple Elements
"""sampleTuple = ("Apple", "Mango", "Banana", "Orange", "Guava", "Berries")     
print("sampleTuple[0] =", sampleTuple[0])  
print("sampleTuple[1] =", sampleTuple[1])  
print("sampleTuple[-1] =", sampleTuple[-1])    
print("sampleTuple[-2] =", sampleTuple[-2])""" 

#Deleting a Tuple
"""sampleTuple = ("Apple", "Mango", "Banana", "Orange", "Guava", "Berries")  
del sampleTuple  
print(sampleTuple)"""

#Concatenation in Tuples
"""a = (1, 5, 7, 9)
b = (2, 4, 6, 8)
c = a + b
print(c)"""


#Repetition of Tuple
"""a = (1, 5, 7, 9, 11)
print(a*2)"""


#Finding the Length of a Tuple
"""a = (2, 4, 6, 8, 10, 12, 14, 16)
print(len(a))"""

#Membership Operators
"""a = (1, 4, 6, 7, 9, 10, 12, 15)
print(11 in a)"""

#Find the maximum element in the Tuple
"""a = (2, 5, 15, 7 ,9)
print(max(a))"""

#Find the minimum element in the Tuple
"""a = (2, 5, 15, 7 ,9)
print(min(a))"""

#Using 'for' loop
"""a = (1, 5, 6, 2, 4)
for i in a:
    print(i)"""

#count() Method
"""a = (1, 4, 5, 7, 9, 10, 4, 4, 11, 4)
count = a.count(int(input("Enter the value")))
print(count)"""

#index() Method
"""a = (1, 4, 5, 7, 9, 11, 15, 19, 20)
index = a.index(int(input("Enter the value : ")))
print(index)"""

#Dictionary
#Set
#Set is mutable but its elements are immutable
"""collection = {1, 2, 3, 4, "hello"}
print(collection)"""

#TypeCasting
"""collection = {1, 2, 3, 4, "hello"}
print(collection)
print(type(collection))"""

#Duplicate value
"""collection = {1, 2, 2, 2, 3, 4, "hello"}
print(collection)"""

#Length
"""collection = {1, 2, 2, 2, 3, 4, "hello"}
print(collection)
print(len(collection))"""

#Empty set
"""collection = set()
print(type(collection))"""

#Set Methods
#Add
"""collection = set()
collection.add(1)
collection.add(2)
collection.add("Hello")
collection.add((7, 8, 9))
collection.add(5)
print(collection)"""

#Remove
"""collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(4)
collection.add(5)
collection.remove(2)
print(collection)"""

#Clear
"""collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(4)
collection.add(5)
collection.clear()
print(collection)"""

#Pop
"""collection = {"hello", "apnacollege", "world", "coding", "python"}
print(collection.pop())"""

#Union
"""set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))"""

#Intersection
"""set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))"""

#Loops
"""i = 1
while i <= 5:
    print("hello")
    i += 1
print(i)"""

i = 1
n = input("Enter the value: ")
while i <= 10 :
    print(i)
    n * i 
    i = i + 1