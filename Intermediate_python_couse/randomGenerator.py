import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# np.random.shuffle(arr)
# The code above demonstrates the use of the numpy library to create a 2D array and then uses the random module from numpy to randomly select elements from that array, maintaining the same shape as the original array.
np.random.seed(10)
print(np.random.rand(arr.shape[0]))
print(np.random.rand(arr.shape[0], arr.shape[1]))
import random
list = [1, 2, 3, 4, 5]
print(random.choice(list))  # Randomly selects and prints one element from the list