import numpy as np
import pandas as pd

arr = np.array([10,20,30,40,50]) # Duplication not allowed in numpy array
print(arr)

a = [10,20,30]
print(a*2) # In list we can't peroform mathematical operation

a1 = np.array([10,20,30])
print(a1*2)

# 2D array(matrix) array
marks = np.array([
    [80,90],
    [70,85]
])
print(marks)
    
# Mean
print("The mean of marks is:",np.mean(marks))
print("The sum of marks:",np.sum(marks))
print("The maximum marks:",np.max(marks))
print("The minimum marks:",np.min(marks))

# Number of rows and columns
print(marks.shape)

# using pandas dataframe

data = {
    'Name':["Riya",'Pritam','Swarup'],
    'Marks':[80,70,90]
}

df = pd.DataFrame(data)
print(df)

# Show the marks column data
print(df['Marks'])
