# tup = (1,2,3,4)
# print(id(tup))
# # tup = (2,3,4)
# # print(id(tup))

# print(tup[0])


# print(type(tup))

# dict1 = {
#     (1,2) : "hello",
#     (1,2) : "hi",
# }
# print(dict1)
# print(id(dict1[(1,2)]))

# list = [1,2,3]

# def myfun(mylist):
#     x =list(mylist)
#     x


list1 = [1,2,3]
list2 = ["A", "B", "C"]
t2 = (7,8,9)

dict1 = {
    'a' : list1,
    'b' : [100, 200, 300],
    'c' : t2,
    'd' : {
        '1' : list2,
        '2' : 'Hello'
    }
}

# dict2 = dict1 # reference copy
# # ab jo bhi hum dict2 mai change krege jo dict1 mai bhi hoga
# # dict2['a'] = dict2['a'].append(1000)
# dict2['a'].append(100)
# print(dict2)
# print(dict1)

# dict2 = dict1.copy()
# dict2['a'].append(101)
# print(dict1)
# print(dict2)

# dict2 = dict1
# dict2['a'].append(101)
# print(dict1)
# print(dict2)





# print(dict1)
# dict2  = dict1
# dict2['b'].append(20)
# print(dict1)

# print(dict1['d']['2'])

# dict2 = dict1
# dict2['d']['1'].append(4)
# dict2['a'].append(4)
# print(list2)
# # print(dict2)
# print(list1)    

# # dict2['b'] = dict2['b'].copy()

# dict1['b'].append(40)
# print(dict1)
# print(dict2)

# dict2 = dict1.copy()
# dict2['b'] = dict2['b'].copy() 
# dict2['b'][0] = 101
# print(dict1)
# print(dict2)


# dict2 = dict1 
# dict2['a'] = dict2['a'].copy()
# dict2['a'].append(400)
# print(dict2)
# print(dict1)

# dict2 = dict1.copy()
# dict2['a'] = dict2['a'].copy()
# dict2['a'].append(400)
# print(dict2)
# print(dict1)


# sort in dictionary
# dict2 = {
#     'b' : 10,
#     'e' : 20,
#     'c' : 30,
#     'a' : 40
# }

# x = list(dict2.keys())
# print((x))
# x.sort()
# print(x)

# for i in dict2:
#     print(dict2[i])


# import pprint

# l1 = [[0] * 10] *10 
# l2 = [l1] * 10
# pprint.pprint(l2)

# l1[1][3] = 1
# pprint.pprint(l1)



# l2 =[]
# for i in range(10):
#     x =[]
#     for j in range(10):
#         x.append(0)
#     l2.append(x)

# pprint.pprint(l2)

# list comprehension

# num = [1,2,3,4,5]
# x = []
# for i in num:
#     x.append(i)
# print(x)


# y = [i for i in num]  # list comprehension
# print(y)


fruits = ["apple" , "banana", "cherry", "kiwi", "mango"]
x  = []
# for i in fruits:
#     if "a" in i:
#         x.append(i)

# print(x)

# y = [i for i in fruits if "a" in i]
# print(y)

# z = [i for i in fruits if len(i)>4]
# print(z)

# x = [i if i!="banana" else "orange" for i in fruits ]
# print(x)



x = ([1,2,3] , [4,5,6])
print(x[0].append(10))
print(x)    


x = "paras pandey"
y = []
y = [i.upper() for i in x]
print(y)

# for i in x:
#     y.append(i.upper())
#     x
# print(y)



