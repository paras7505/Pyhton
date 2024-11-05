# s = 'hello world'
# s1 = "hello world"
# s3 = """ hello "world"  """
# s4 = ''' hello world ''' 
# print(s)
# print(s1)
# # print(s2)
# print(s3)
# print(s4)



# # for i in s:
#     # print(i)


# s = 'this is a string'
# print(s[0])
# print(s[-1]) # we can also do negative indexing 


# # s= 'hello'
# print(s*3)

# print(len(s))


# result = s.split(" ")
# print(result)
# newString = "_".join(result)
# print(newString)


# # string formatter
# # here we put the placeholder in the {}

# string = " his name {0}. he like' {1}"
# print(string.format('paras','football'))


# string1 = " he is {name}. he like's {sports}"
# print(string1.format( name = 'paras' , sports = 'football'))


# # string modifier

# s =  "the rate fo the apple is Rs{price:.2f} per Kg"
# print(s.format(price =  45.13353268321))

# s =  "the rate fo the apple is Rs{price:,} per Kg"
# print(s.format(price =  4513353268321))


# print( f"we can use the string as the operation by using f in front of the strings {5+5}")

# def calculate(x):
#     return x + 10

# x = 22
# s = f'this is out string {calculate(x)}'
# print(s)

# x = 0.23

# s = f"this is percentage {x:.0%}"
# print(s)



# def fun1():
#     def fun2():
#         def fun3():
#             print('printing function 3')
#         fun3()
#         print("printing function 2")
#     print('printing function 1') # ye funciton1 hai
#     fun2()
# fun1()




# #******************* file handling *********************

# a = open("demo.txt")
# print(a)
# print(a.read(10))
# print(a.read())

# a2 = open("demo.txt", "r")
# x = a2.readlines() # it will return the character in array
# print(x)


# # a3 = open("demo3.txt", "a") # here the new file is crated open a file in append mode if not exists then it will create a new file

# f = open("demo.txt" , "a")
# f.write("\nthis is a new line ")
# f.close() # always close the file after writing in the file  



# f2 = open("demo4.txt" , "a")
# f2.write("add a new line ")
# f2.close() 

# k1 = open("demo.txt" , "a")
# k2 = open("demo.txt" , "a")

# k1.write("\nhello world")
# k2.write("\nhello world 2")

# k2.close()
# k1.close()

# x = input()
# k3 = open("demo.txt" , "a")
# k3.write(x)
# k3.close()

# f = open("demo3.txt" ,"w") # here if we open file in write mode then the previous data is erased
# f.write("helllo world \n welcome")
# f.close()

# # we have a formate to automatically close the file 

# with open("demo3.txt" , "w") as v:
#     v.write("hello world 2 \n this is a way we don't need to close file ")

# with open("demo3.txt") as c:
    # print(c.read())
    # print(c.tell()) # it tells the location of the pointer
    # print(c.readline())
    # print(c.seek(20))
    # print(c.readline())


# with open("demo3.txt" , "a") as v:
#     # print(v.readlines()) # in append mode the reading is not allowed  
#     print(v.tell())    
#     v.seek(50)
#     print(v.tell())
#     v.write("hello world again 5") 
#     v.tell()
#     v.seeK(offset)
#     v.seeK(59)     
#     # error hai seek change nahi hora hai 


# with open("demo.txt", "w") as f:
#     f.write("hello world\n")
#     f.write("how are you\n")
#     f.seek(5,1)
#     print(f.tell())






# with open("demo5.txt", "a") as f:
#     f.write("hello we are learing pyhton file handling\n")

# with open("demo5.txt", "r") as f:
#     x = f.readlines()
# print(x)

# x[1] = "pyhton file handling\n"
# with open("demo5.txt" , "w") as f:
#     f.writelines(x)         


# CSV Reading 
# csv are comma seperated values 

import csv

with open("demo.csv") as csvfile:
    # filereader = csv.reader(csvfile)
    filereader = csv.DictReader(csvfile)
    # print(next(filereader)) # it only read one file at a time 
    # we can use for loop for printing the all the value 
    for i in filereader:
        print(i)

# count no. of occurance of substring 
x = 'a'
def count(str):
    count = 0
    for i in str:
        if(i==x): 
            count+=1
print(count)

count("parasPandey")

# str1 = "paras pandey"
# count = 0
# for i in str1:
#     if(i=='a'):
#         count+=1
# print(count)


# def fun(str):
#     count = 0
#     for i in str:
#         if(i=='a'):
#             count+=1

#     print(count)
# fun("paras Pandey")

import pprint
l2 = []
for i in range(10):
    x = []
    for i in range(10): 
        x.append(0)
    l2.append(x)
# pprint.pprint(l2)

l2[1][0] = 23

# pprint.pprint(l2)




import math

print(math.ceil(-3.3)) # it will give the larger value
print(math.floor(-3.3)) # it will give the smaller value 

from datetime import datetime
d = datetime.now()
print(d)
print(d.year)
print(d.strftime("%a"))

import Mymodule

Mymodule.gretting("paras")
