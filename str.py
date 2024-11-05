s = 'hello world'
result = s.split(' ')
print(result)
new = "_".join(result)
print(new)


# str = ''' hello ji kya hal .
# ki hal hai '''
# print(str)


# # string formatting 

# s1 = "his name is "
# s2 = "he likes "
# print(s1 +"paras" + " " + s2 + "badminton" )


# s = "his name is {0} ,{0}  he likes {1}"
# print(s.format("paras" , "football"))


# # we can add keyword arguments 
# s = "his name is {name} ,{name}  he likes {sports}"
# print(s.format(name = "paras" , sports ="football"))


# s = "the apple price is Rs {:.2f} per kg"
# print(s.format(45))

# s = "the apple price is Rs {:c} per kg"
# print(s.format(45))

# s = "the apple price is Rs {price:<8} per kg"
# print(s.format(price = 45))


# x = 34
# s = f"this is our string : {x:.2f} " #f = formatting 
# print(s)

# s = f"this is our string : {35+5} " #f = formatting 
# print(s)


# x =100
# def fun1():
#     x = 99999
#     def fun2():
#         x = 'hello'
#         def fun3():
#             x = "gn"
#             print(x)
#         fun3()
#     fun2()
# fun1()
