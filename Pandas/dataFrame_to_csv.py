import pandas as pd

data = {
    'course' : ["pyhton" , "cpp" , "javascript"],
    'mentor ' : ["xyz" ,"abc" , "pqr" ]
}
df = pd.DataFrame(data)
print(df)


df.to_csv("adding.csv")


df = pd.read_csv("adding.csv")
print(df)