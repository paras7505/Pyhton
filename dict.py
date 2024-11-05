# dict1 ={
#      'subject': "python",
#      'author' : "rajat jain",
#      'course' : "Fynd"
#     }

# print(dict1)

# print(dict1['author'])
# print(dict1.get('author1')) # another way to get the values but it will not give error if it does not exists
# print(dict1.keys())
# print(dict1.values())

# dict1['course'] = "fynd academy" # upadate the value

# print(dict1)

# # update the values in the dict

# dict2 = {
#     'author': "paras",
#     'paras' :"pandey",
#     'a': 2534
# }
# dict1.update(dict2)
# print(dict1)

# print(dict1.items())

# del dict1['a']
# print(dict1)
# # we also have pop to delete value but this return the value which is poped out
# x = dict1.pop('author')
# print("deleted value is :" , x)
# print(dict1)
# dict1.clear()
# print(dict1)



# # t1 = (12,'paras' , 33)
# # print(type(t1))
# # print(t1)

# # print(id(t1))
# # print(t1[0])
# # t1[0] = 23
# # print(t1)

# f1 = ({
#     'key1' : 'val1',
#     'key2' : 'val2'
# })
# print(f1)
# print(type(f1))




# f1 = (12,45)
# print(type(f1))
# print(f1)


# def myfun():
#     return (34,55)

# x = myfun()
# print(x[0], x[1])


# list1 = [1,2,3]

# def myfun(mylist):
#     mylist.append(5)
#     print('inside', mylist)
# # here without returing the values are changing cause of we are passing reference of the list1 we are not copying 

# myfun(list1)
# print("outside", list1)

list1 = (1,2,3)

def myfun(mylist):
    x = list(mylist)   # here it is creating new reference in this the change will happen
    x.append(5)
    print('inside', x)
    print(id(mylist))
    print(id(x))

#in this the values will change because we make it as tuple and if we want to make any change so we will make a copy of that and then we do

myfun(list1)
print("outside", list1)
print(id(list1))



x = [1,2,3]
# y = x
# y.append(4)
# print(y)
# print(x)
# print(id(x))
# print(id(y))

y = []
for i in x:
    y.append(i)
y,append()
print(y)
print(x)