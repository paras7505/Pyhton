# function 
yy = 55
def paras(a,b):
    result = a-b
    global yy # bad practise 
    yy = 99
    return result

x = paras(5,3)
print(x)
print(yy)



# def myfun(name):
#     return "hello" + name + "!" 

# a = myfun(paras)
# print(a)


# def myfunction(firstName , lastName):
#     print("hello " + firstName + " " +lastName)

# myfunction("paras", "pandey")

def fun(name, last = "pandey"):
    print("hello " + name + " " + last)

fun("paras")


def rec(n):
    if n==1:
        return 1
    return n*rec(n-1)

def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)



print(rec(5))
print(sum(3))
# aribitary 


def greet(firstName , lastName):
    inside  = 20 # this inside variable has different scope 
    def fullName():
        inside = 30 # this inside has different scope
        print(inside)
        return firstName + " " + lastName

    print("hello" , fullName())
    print(inside)

greet("paras","pandey")



def shout(text):
    return text.upper()

def whisper(text):
    return  text.lower()

def greet(func):
    x = func("the quick brown fox")
    print(x)

greet(shout)
greet(whisper)

for i in range(20):
    if i%2==0:
        print(i)




def mm():
    print("hello")

abc = mm
abc()


funct = lambda x,y: x+y
print(funct(5,5))

