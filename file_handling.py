# f = open('demo.txt')
# print(f)
# print(f.read(10))
# print(f.read(10))
# print(f.read(10))
# print(f.read(10))
# print(f.read(10))
# print(f.read())

# # r = read
# # a = append
# # w = write
# # 

# f = open("demo.txt" ,"a")
# f.write("\n this is line 3")
# f.close()
# print(f.read())


# f = open("demo.txt" ,"a")
# print(f.read())



# f = open('demo.txt', "a")

# x =input("enter the data:  ")
# f1= open("demo2.txt" , "a")
# f1.write(x)


def length(a):
    count = 0
    for i in a:
        count +=1
    return count
length([1,2,3,4,5])
