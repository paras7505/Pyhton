# class car:
#     wheels = 4 # attribute 
#     color = "white" 

#     def getdetail(self): # method
#         print("color of the car is " , self.color)

# car1 = car() #instance/object
# car2 = car()

# print(car1)
# print(car2)

# print(car1.color)
# print(car2.color)
# car2.color = "black"
# print(car2.color)
# car1.color="red"
# car1.getdetail()
# car2.getdetail()

# car1.wheels = 100
# car1.color = "green"
# print(car1.wheels)
# print(car1.color)




# class bike:
#     wheels = 2
#     engine = 1

#     def method(self):
#         print("the engine on the bike is : " , self.engine)

# spShine = bike()
# hfDelux = bike()

class car:
    wheels = 4

    def __init__(self,color, seat):
        self.color = color
        self.seat = seat

    def getDetails(self):
        print(self)
        print("color of the car is : ",self.color)

car1 = car('black',4)
car2 = car('white', 6)

# print(car1.color, car1.seat)
# print(car2.color, car2.seat)
# car1.getDetails()

# car.getDetails(car2)
# car2.getDetails()



# class computer:
#     def __init__(self,processor, memory):  # constructor
#         self.processor = processor
#         self.memory = memory

# c1= computer('i7', '8gb')
# c2= computer('i3', '4gb')
# print(c1.memory,c1.processor)
# print(c2.memory,c2.processor)
# print(c1)

# print(type(computer))


class computer:

    def __init__(self,memory, processor):
        self.memory = memory
        self.processor = processor

    def setProcessor(self, newvalue):
        self.processor = newvalue
    
    def getprocessor(self):
        return self.processor

    def getcarcolor(self):
        print("The color of the car is:",self.color)

c1 = computer("4gb" , "i5")
c2 = computer("8gb" , "i7")

c1.setProcessor('i8')
print(c1.getprocessor())

