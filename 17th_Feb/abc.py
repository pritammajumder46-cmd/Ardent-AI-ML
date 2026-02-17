# Converting Lists into DataFrame
import os
import numpy as np
import pandas as pd

os.system("cls")

student_info = [
    ['Ankita',22,'SVU',300000],
    ['Pritam',20,'SVU',340000],
    ['Ankur',20,'SVU',340000],
    ['Soumyadip',21,'SVU',400000]
]

# print(student_info)

# ADD COLUMNS
df = pd.DataFrame(student_info,columns=['Name','Age','College','Fees'])
print(df.to_string(index=False))

df.to_csv("Student_info.csv",index=False) # Creating this as a CSV File

A = np.array([
    [1,2,3],
    [4,5,6]
])

B = np.array([
    [7,8,9],
    [1,2,3]
])

print(A+B)
print(A-B)
print(A*B)
print(A/B)

# ARRAY INDEXING
x = np.array([1,2,3,4])
print(x[0])
print(x[1])
print(x[2])
print(x[3])

#2D 
arr  = np.array(
    [
        [1,2,3,4,5],
        [6,7,8,9,10]
    ]
)

print(arr[0,0]) # PRINTS 1
print(arr[0,1]) # PRINTS 2
print(arr[0,2]) # PRINTS 3
print(arr[0,3]) # PRINTS 4
print(arr[0,4]) # PRINTS 5