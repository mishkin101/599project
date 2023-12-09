
from Game import Game
import numpy as np


# Define the array
array = np.array([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])

# Select the largest negative value in the last row
largest_negative = np.max(array[-1, array[-1] < 0])

# Replace nan values with a specific value
largest_negative = np.nan_to_num(largest_negative, nan=-1)

print(largest_negative)
print(np.identity(0))
# Define the numpy matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the unique elements
elements = np.array([1, 2, 3])

# Multiply every row in the matrix by a unique element
result = matrix * elements[:, np.newaxis]

print(result)