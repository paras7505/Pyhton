# list1 = [1,2,3]
# list2 = ["A","B","C"]
# t2 = (7,8,9)

# dict1 = {
#     'a' : list1,
#     'b' : [100,200,300],
#     'c' : t2,
#     'd' :{
#         '1' : list2,
#         '2' : 'hello'
#     }
# }
# dict1['d']['name'] = 'paras'
# print(dict1)
# dict2 = dict1.copy() 

# dict1['b'].append(5)
# print(dict1)
# print(dict2)


# print(id(dict1))
# print(id(dict2))
# # print("printing dict2 ",dict2)
# # print("printing dict1",dict1)

# # dict1['d']['1'].append(5)
# # print(list2) 
# # print(list1)
# # print(dict1)
# # print(dict2)    

# x = [5,6]
# list1 = [1,2,x]
# print('printing list 1',list1)
# list2=list1.copy()
# print('printing list 2',list2)
# x.append(7)
# print('printing list 1',list1) # referece ka reference change nahi hota hai kahli bhar vala usko shallow copy bolte hai 
# print('printing list 2',list2)
# list2.append(10)
# print('printing list 2',list2)
# print('printing list 1',list1)


# # if we have to make change in the inner reference then we have to make the copy of the inner reference
# # here we go 
# dict3 = dict1.copy()
# dict3['b'] = dict1['b'].copy()
# dict3['b'].append(50)
# print(dict3)
# print(dict1)
# print(dict2)


# list1 = [1,2,3]
# list2 = ["A" , "B", "C"]
# t2 = (7,8,9)
# dict1 = {
#     'a': list1,
#     'b':[100,200,300],
#     'c': t2,
#     'd':{
#         '1': list2,
#         '2': 'hello'
#     }
# }
# print(dict1)
# dict2 = dict1.copy()
# print(dict2)
# dict2['d']['3'] = "world"
# print(dict2)
# print(dict1)

# dict2['a'] = list1.copy()
# dict2['a'].append(20) 
# print(dict1)
# print(dict2)

# dict2['b'] = dict1['b'].copy()
# dict2['b'].append(400)
# print(dict1)
# print(dict2)


# dict2 = {
#     'b' : 10,
#     'e' : 20,
#     'a' : 30,
#     'c' : 40
# }

# x = list(dict2.keys())
# x.sort()
# print(x)
# for i in x:
#     print(dict2[i])


# 2D list 

# x = [[1,2,3],[4,5,6],[7,8,9]]
# print(x)
# y = x.copy()
# y[0]= x[0].copy()
# y[0][0] = 50
# print(y)    
# print(x)    
 
# import pprint
# l1 = [0] * 10
# l2 = [l1] * 10
# # pprint.pprint(l2) 
# l2[1][3]= 100
# # pprint.pprint(l2)

# print('\n')

# l3 =[[0] * 10] * 10
# # pprint.pprint(l3)
# print('\n')

# l3[1][3] = 1
# # pprint.pprint(l3)

# print('\n')



# l4 = [0] * 10
# l5 = []

# for i in l4:
#     l5.append([0]*10)

# pprint.pprint(l5)


# l5[1][3] = 1
# pprint.pprint(l5)


# we can also do like we used to do * pattern

# l6 = []
# for i in range(10):
#     x = []
#     for j in range(10):
#         x.append(0)
#     l6.append(x)

# l6[1][3] = 1
# pprint.pprint(l6)

# list comprihenshion 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


x = []
for i in fruits:
    x.append(i)

print(x)

y = [ i for i in fruits] # in this the value will got append in the y 
print(y)


z = []
for i in fruits:
    if 'a' in i:
        z.append(i)
print(z)

# short 
# a = [i for i in fruits if 'a' in i]
a = [i for i in fruits if len(i)>4]
print(a)


x = "hello world"
y = list(x)
print(y)
# y.upper()
# print(y)

y = [i.upper() for i in x]
print(y)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
d = []
for i in fruits:
    if i !='banana':
        d.append(i)
    else:
        d.append("orange")
print(d)


d = [i if i!='banana' else ("orange") for i in fruits]
print(d)            


dict1 = {
    ([1,2,3]) : "hello"  # here we cannot use the tuple as the key 
}
print(dict1) 