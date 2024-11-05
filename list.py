# # list 

# paras = ['paras' , 'pandey' , 24 ,45 , True , False]
# print(paras[3])

# # list inside list :- nested list 

# pa = ['paras' , 'pandey' , 24 ,45 , True , False, [100,200,300]]
# print(pa[6][1])

# print(pa[0][0]) # by this we can access the index of the string 

# val1 = []
# val1.append(3)
# val1.append(4)
# val1.append(1)

# print(val1)

# val1.sort()

# print(val1)

# # we can also append list inside list 

# val1.append(['paras', '[pandey]'])
# print(val1)

# del val1[3][1]
# print(val1)

# arr1 = []
# for i in range(10):
#     arr1.append(0)
# print(arr1) 

# arr2 = ['paras']*10
# print(arr2)


# # negative indexing 

# arr3 = [1,2,3,3,4,5,75]
# print(arr3[-1])
# print(arr3[-2])
# print(arr3[-3])
# print(arr3[-4])
# print(arr3[-5])
# print(arr3[-6])


# slicing 
# x = ['the quick brown fox jums over the lazy dog']
# print(x[4 : 10])

# x = ['the ', 'qucik' , 'jas' , 'absf']
# print(x[0: ])

# a = [1,2,3]
# b = [4,5,6]
# # print( a + b)

# for i in b:
#     a.append(i)
# print(a)
# print(b)


# soritng

# arr = [651,5,135,31,5351,32135]
# arr.sort()
# print(arr)

# arr2 = sorted(reverse=True)
# print(arr2)


a = [1,2,3]
y = a
y +=[4,5]
print(a)
print(y)