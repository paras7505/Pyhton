
# var = {1,"paras" , "pandey" , 45,236,8}
# print(var)
# print(type(var))

# for i in var:
#     print(i)


# list1 = list(var) #convert set to list 
# print(list1)


# var2 = {"this" , "is"}
# var.update(var2)
# print(var)


# # s1 = {'a', 'b' , 'c' , ' d'}
# # s2 = {'c' , 'd'}

# # s1 = {'d' , 'e'}
# # s2 = {'d' , 'e'}

# s1 = {'e' , 'd'}
# s2 = {'d' , 'e'}


# print(s1==s2)
# print(s1) 

# s = s1.union(s2)
# print(s)


# print(s1.union(s2))

# print(s1)
# print(s2)

# union 

# s1 = {'a', 'b' , 'c' , 'd'}
# s2 = {'c', 'd'}

# s3 = s1.union(s2)
# print(s3)

# # intersection 

# s3 = {'a','b', 'c' , 'd'}
# s4 = {'b' , 'd'}

# s5 = s3.intersection(s4)
# print(s5)
# print(s1 & s2)

# #difference in set 
# s6 = s4-s3
# s6 = s3-s4
# print(s6)



# dictinory

dict1 = {
    'name' : 'paras',
    'age' : 999,
    'bool': True,
    True : 34,
    'age' : 'hello',
    (1,2):'try==='
}

print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1['cllg'] = ['aps'] # by this we can add new value 
print(dict1)
dict1.pop('age')
print(dict1)
del dict1['name']
print(dict1)
# print(dict1[(1,2)])
# print(dict1.get('name'))
# print(len(dict1))

# print(hash("paras"))