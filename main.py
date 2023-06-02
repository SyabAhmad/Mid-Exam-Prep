# Mid Exam Preparation
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

print(data.iloc[[0, 2], :])

