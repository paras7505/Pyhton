class Myclass:
    var1 = 10
    var2 = 20
    var3 = 30
    var4 = 40

obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj4 = Myclass()

# print(obj1.var2)
# print(obj2.var1)
# print(obj3.var4)
# print(obj4.var3)

obj1.var1 = 100
# print(obj1.var1)



# class car:
#     wheels = 4
#     color = "white"

#     def get(self):
#         print("the color of the car is:",self.color)

# car1= car()
# car2 = car()
# car1.color = 'red'
# car1.get()
# car2.get()


class car:

    wheels = 4

    def __init__(self, color,seat):
        self.color = color 
        self.seat = seat

    def get(self):
        print("the color of the car is:",self.color)
        print("The no. of seat in the car are:",self.seat)

   

# car1= car("black",5)
# car2 = car("red",4)
# print(car1.seat)
# print(car1.color)
# car1.color = "green" # we can change the color of the car 
# car1.get()
# car2.get()



class computer:

    def __init__(self,memory, processor):
        # self.memory = memory
        self.__memory = memory # by puting __ we make it as private we can not access this value but by getter we can access it
        self.processor = processor
    
    #setter and getter

    def setProcessor(self, newvalue):
        if(newvalue =='i3' or newvalue == 'i5' or newvalue == 'i7'):
            self.processor = newvalue
        else:
            raise ValueError("this is not a valid input")
    
    def getprocessor(self):
        return "processor:" +  self.processor
    
    def getmemory(self):
        return self.__memory

    def getdetail(self):
        print('the memory of the computer is:',self.memory)
        print('the memory of the computer is:',self.processor)

c1 = computer('4gb', 'i5')
c2 = computer('6gb', 'i7')

# print(c1.memory)
# print(c1.processor)
# c1.getdetail()
# c2.getdetail()

# print("the processor of c1:",c1.processor)


c1.setProcessor("i7")
# print("processor of c1 ",c1.processor)
# print(c1.getprocessor())

# print(c1.getmemory())


import random
class bank():

    def __init__(self, accountName, balance = 0):
        self.__isopen = True
        self.accountName = accountName
        self.accountNumber = int(random.random() * 100)
        self.__balance = balance

    def creditAmount(self,amount):
        if(amount > 1 and self.__isopen):
            self.__balance += amount
        else:
            raise TypeError("this account is closed")

    def debitAmount(self,amount):
        if(amount<self.__balance and self.__isopen):
            self.__balance -=amount
            # print("balance:",self.checkBalance())
            # print(bank.checkBalance(acc1))
            return amount
        else: 
            print("insufficient money")
    
    def checkBalance(self):
        return self.__balance
    
    def __add__(self, other):
        newBalance = self.__balance + other.__balance
        self.__balance = 0
        other.__balance = 0
        other.__isopen = False
        self.__isopen = False
        return bank(self.accountName,newBalance)  # returning new object of account 


    def getBankDetails(self):
        print("the account holder name:",self.accountName)
        print("the account number is:",self.accountNumber)
 

    def __str__(self):
        return "account number :" + str(self.accountName)

acc1 = bank("paras pandey" , 100)
acc2 = bank("rohit rawat", 200)
print(acc1.checkBalance())
print(acc2.checkBalance())

# print("the debited amount is:",acc1.debitAmount(25))

# print("the details are",acc1.getBankDetails())
acc1.getBankDetails()

acc3 = acc1 + acc2
print("new acccount balance", acc3.checkBalance())
acc3.accountName
print('check balance', acc1.checkBalance()) # it is closed now
print('check balance', acc2.checkBalance()) # it is closed now 
print('check balance', acc3.checkBalance())

# print(acc3.accountName)
# print(acc3.accountNumber)
print(acc1)
print(acc2)
print(acc3)

# print(acc1.checkBalance())
# print(acc3.checkBalance())
# print(acc2.checkBalance())





# self represents the current instance of the class

class car:

    def __init__(self, color,seat):
        self.color = color 
        self.seat = seat
    
    # def __init__(v, color,seat): # we write it as v variable, it is just a variable name it is industry standard
    #     v.color = color 
    #     v.seat = seat

    def getdetail(self):
        print(self)
        print("the color of the car is:",self.color)
        print("The no. of seat in the car are:",self.seat)

c1 = car("white", 4)
c2 = car('black', 4)
# print(c1)
# print(c2)
    
# c1.getdetail()
# c2.getdetail()
