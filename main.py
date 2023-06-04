# Mid Exam Preparation for DataScience
# list of Numpy operations

import numpy as np
import pandas as pd

# ----------------------------------------------------------------
# numpy basic operations
arr = np.array([1,2,3,4,5,6,6,7])
# Printing array
print(arr)

# mean of the array
print(arr.mean())

# standard deviation of the array
print(arr.std())

# sorting array
print(np.sort(arr,)[::-1])

# addition of two arrays
arr2 = np.array([1,2,3,4,5,6,6,7])
arr3 = np.add(arr2, arr)
print(arr3)

# multiplications of two arrays

arr4 = np.dot(arr, arr2)
print(arr4)

# max
print(np.max(arr))

# min
print(np.min(arr))

# find sum
print(np.sum(arr))

# find unique
print(np.unique(arr))

# Reshaping
reshapedArray = np.reshape(arr, (-1))
print(reshapedArray)

# indexing in numpy and where function
index = np.where(arr==6)
print(index)

# pandas basic operations

data = {"Names":['mike',
                 'john',
                 'bob',
                 'alice'],
        "Age":[15,
               12,
               64,
               34],
        "location":['new york',
                'mingora',
                'kokrai',
                'islamabad']
        }

print(data)

# print DataFrame

data = pd.DataFrame(data)
print(data)

# printing specific multiple rows and columns
print(data.iloc[[0, 2], :])
print(data.iloc[[0,1,2], :2])
# print(data.head(2).tail(2))
# to write to CSV file
data.to_csv('data.csv', index=False)

# to write file to excel we must import necessary libraries
# import openpyxl
# data.to_excel('data.xls', index=False)

# Adding a new column
data["GPA"] = [3,4,2.2,3.4,]
print(data)

# finding average GPA in DataFrame

average = data["GPA"].mean()
print(data['GPA'].max())
print(data['GPA'].min())
print(data['GPA'].std())
print(average)

# Filtering dataset
for index, line in data.iterrows():
    # if GPA is greater then 3 show all rows and columns
    if line["GPA"] > 3:
        print(line)

# Filtering dataset
for index, line in data.iterrows():
    # want to look for specific column
    if line["Names"] == 'bob':
        print(line)
