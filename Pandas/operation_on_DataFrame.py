import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Julia', 'Kevin', 'Linda'],
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'HR', 'IT', 'HR', 'Marketing', 'Finance', 'IT', 'Marketing', 'HR'],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'M', 'F'],
    'Salary': [70000, 85000, 95000, 90000, 60000, 100000, 72000, 65000, 88000, 110000, 68000, 75000],
    'Experience': [5, 10, 12, 8, 4, 15, 6, 7, 11, 13, 5, 8]
}

df = pd.DataFrame(data)
# print(df)


result = df.groupby('Department')
print(result)

for a , b in result:
    print(a)
    print(b)
    print()


print(result.get_group('Finance'))



