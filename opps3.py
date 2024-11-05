# class car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model
#     def getdetail(self):
#         print("the brand of the car is:",self.brand)
#         print("the model of the car is:",self.model)

#     def welcome(self):
#         print("welcome to the car showroom")



# c = car('honda',5201)
# c2 = car('maruti',2012)
# c.welcome()
# print(c.brand)
# print(c.model)
# c.getdetail()
# c2.getdetail()

# class student:
#     def __init__(self ,name, marks):
#         self.marks = marks
#         self.name = name
    
#     def get_avg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print(f"{self.name} has the average marks of {sum/3}")

# s1 = student("paras",[12,7,52 ])
# s1.get_avg()    



#abstraction 

class car:
    def __init__(self):
        self.acc= False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch =True
        print("car stated..")

# c = car()
# c.start()

class account:
    def __init__(self,accountno,accountname,balance):
        self.accountname = accountname
        self.accountno = accountno
        self.__balance = balance

    def credit(self , creditAmount):
        self.__balance += creditAmount
        return creditAmount

    def debit(self , debitAmount):
        if debitAmount < self.__balance:
            self.__balance -= debitAmount
            return debitAmount

    def checkbalance(self):
        return self.__balance

acc1 = account("paras" , 10, 100)
print(acc1.credit(5))
print(acc1.checkbalance())
print(acc1.debit(50))
print(acc1.checkbalance())