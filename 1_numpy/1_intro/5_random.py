import numpy as np

# generate an array of 5 random numbers
array = np.random.rand(5)

print(array)

# n-d arrays with np.random.rand

# create a 2D array of 2 rows and 2 columns of random numbers
array1 = np.random.rand(2, 2)

print("2-D Array: ")
print(array1)

# create a 3D array of shape (2, 2, 2) of random numbers
array2 = np.random.rand(2, 2, 2)

print("\n3-D Array: ")
print(array2)
