import pandas as pd 

print(pd.__version__)   


# data = {
#     'course' : ["pyhton" , "cpp" , "javascript"],
#     'mentor ' : ["xyz" ,"abc" , "pqr" ]
# }

# newdataframe = pd.DataFrame(data)
# print(newdataframe)

# comma seperated values

df = pd.read_csv("sample.csv")
print(df)


# we can also read the josn file 

df = pd.read_json("myjson.json")
print(df)




