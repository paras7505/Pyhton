# inheritance in python 

class person:

    def __init__(self , name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"person name is: {self.name} and id is: {self.id}")

class employee(person):
    def __init__(score, post):
        self.score = score
        self.post = post
        person.__init__(self,name, id) # to inherit the class 


    def display(self):
        print(f"person name is: {self.score} and id is: {self.post}, score is:{self.score} , post is :{self.post} ")

class tester(employee):
    def __init__(self, name , id , score, post):
        employee.__init__(self, name, id , score, post)

# x = tester("paras" , "123", 45, "sde")
# x.display()
# y = employee(56,"ceo")
# y.display()



class ClassA:
    def __init__(self):
        self.a = 1
        print('contructor of A')
    def method(self):
        print("m1")

class ClassB:
    def __init__(self):
        self.a = 2
        print('contructor of B')
    def method(self):
        print("m2")

class classC(ClassB, ClassA):
    def __init(self):
        print("contructor of c")
        ClassB.__init__(self)
        classA.__init__(self)   
        # ClassA.__init__(self)
    def method(self):
        # ClassA.method(self)
        # ClassB.method(self)
        print("m3")

c = classC()
c.method()
# print(c.a)



# ecapsulation 

# class classA:
#     def __init__(self,b):
#         self.a = "hello"
#         self.__b = b

#     def __getB(self):
#         return f"organisation : {self.__b} " 

#     def get(self):
#         return self.__getB()

#     def setB(self, value):
#         self.__b = value

# c = classA('Fynd')
# print(c.a)
# c.setB("")
# print(c.get())


# class classA:
#     def __init__(self, b):
#         self.a = "hello"
#         self.__b = b

#     def setB(self, value):
#         self.__b = value

#     def getb(self):
#         return self.__b

# c = classA('bye')
# print(c.a)
# print(c.getb())
# c.setB("paras")
# print(c.getb())

from abc import ABC , abstractmethod


class animal:
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def talk(self):
        pass

class cat(animal):
    def __init__(self,name):
        super().__init__(name)
    def talk(self):
        return " meow !!"
    def eat(self):
        return "cat food"

class dog(animal):
    def __init__(self, name):
        super().__init__(name)
    def talk(self):
        return "woof woof !!"
    def eat(self):
        return "dog food"

class Lion(animal):
    def __init__(self,name):
        super().__init__(name)
        

# creating object
x = dog("rohit")
print(x.talk())
y = cat("puchhchu")
print(y.talk())

listt = [ dog("dog1") , cat("cat1") , cat("cat2") , dog("dog2") , dog("dog3")]
for i in listt:
    print(type(i))
    print(i.name + " : " + i.talk() + " eats " + i.eat())
    print("------------")