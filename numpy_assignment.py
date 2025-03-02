#1
import numpy as np

array_1d = np.arange(1, 21)

#1A
sum_array = np.sum(array_1d)
mean_array = np.mean(array_1d)
median_array = np.median(array_1d)
std_dev_array = np.std(array_1d)
print(f"Sum: {sum_array}, Mean: {mean_array}, Median: {median_array}, Standard Deviation: {std_dev_array}")

#1B
indices_greater_than_10 = np.where(array_1d > 10)
print(f"Indices of elements greater than 10: {indices_greater_than_10}")

#2
#2A
array_2d = np.arange(1, 17).reshape(4, 4)
print("Original 2D Array:")
print(array_2d)
print("Array printed above")

#2B
transpose_array = np.transpose(array_2d)
print("Transposed Array:")
print(transpose_array)

#2C
row_sums = np.sum(array_2d, axis=1)
col_sums = np.sum(array_2d, axis=0)
print(f"Row-wise sums: {row_sums}")
print(f"Column-wise sums: {col_sums}")

#3
array_1 = np.random.randint(1, 21, size=(3, 3))
array_2 = np.random.randint(1, 21, size=(3, 3))
print("Array 1:")
print(array_1)
print("Array 2:")
print(array_2)

#3A
addition_result = np.add(array_1, array_2)
subtraction_result = np.subtract(array_1, array_2)
multiplication_result = np.multiply(array_1, array_2)
print("Element-wise addition:\n", addition_result)
print("Element-wise subtraction:\n", subtraction_result)
print("Element-wise multiplication:\n", multiplication_result)

#3B
dot_product = np.dot(array_1, array_2)
print("Dot Product:\n", dot_product)

#4
array_1d_12 = np.arange(1, 13)
reshaped_array = array_1d_12.reshape(3, 4)
sliced_array = reshaped_array[:2, -2:]
print("Reshaped Array:")
print(reshaped_array)
print("Sliced Array (First two rows, last two columns):")
print(sliced_array)
