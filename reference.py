
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]

# d = [100,200,300]
# arr = [a,b,c] 
# arr2 = arr.copy()

# arr2[0] = d
# print(arr)
# print(arr2)


# arr = [a,b,c] 
# arr2 = [a.copy(), b.copy() , c.copy()] 
# arr2[0][1] = 100 
# print(arr) 
# print(arr2) 



l1 = [1,2,3]
l2 = l1.copy()
l2[0] = 4
print(l1)
print(l2)




d = [100,200 , 300]
arr = [[1,2,3],[4,5,6],7]
arr2 = arr.copy()
arr2[1] = arr2[1].copy()
# arr2 = arr

arr2[1][0] = 100  # deep copy 
arr2[0][1] = -10 
arr2[2] = 5
print(arr)
print(arr2)
