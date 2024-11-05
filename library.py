import datetime
x = datetime.datetime.now()
print(x)


from datetime import datetime
y = datetime.now()
print(y)


x = datetime.now()
print(type(x))
print(x.year)
print(x.strftime("%d-%B-%Y-%A"))