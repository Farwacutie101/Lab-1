import numpy as np

#1. Create a rank 2 (2D) array that resembles the matrix below.
# Create the array
matrix = np.array([[11, 12, 13, 14],
                   [15, 16, 17, 18]])
print(matrix)

# Use the appropriate functions to solve the following questions

# 1. Create an array with 4 rows and 3 columns of zeros.

array = np.zeros((4, 3))
print(array)

# 2 .Create an array of ones that has 3 rows and 4 columns
array = np.ones((3, 4))
print(array)

# 3) Create an array containing integers 4 to 13 inclusive.
array = np.arange(4, 14)
print(array)

# 4) 4. Create an array containing
# [0., 1.5, 3., 4.5]
array = np.array([0.0, 1.5, 3.0, 4.5])
print(array)

# 5)  Create a 2 by 2 array containing '4' in each position.
array = np.full((2, 2), 4)
print(array)

#6  Create 2 matrices:
# i. Identity matrix of size 4
identity_matrix = np.eye(4)
print(identity_matrix)

#ii. Diagonal matrix with [10,12] as the diagonals
diagonal_matrix = np.diag([10, 12])
print(diagonal_matrix)

# 7 ) Create a 3 by 3 array with random floats in [0, 10].
array = np.random.uniform(0, 10, size=(3, 3))
print(array)

# 8) Create a 3 by 3 array with random integers in [10, 20].
array = np.random.randint(10, 21, size=(3, 3))
print(array)

############ SLICING ARRAYS #######

# 1)  # Define the array
myArray = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])

# # Get the subarray of the first row and first 2 columns
myArray = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])

# a. Get a subarray of the first row and first 2 columns
subarray_a = myArray[0, :2]
print("Subarray a:", subarray_a)

# b. Change all elements in 1st and second row to 0
myArray[:2, :] = 0
print("Array after changing elements in the 1st and 2nd rows to 0:")
print(myArray)

#2. Create an array containing integers from 0 to 20 and reverse the order.
original_array = np.arange(21)

# Reverse the order of the array
reversed_array = original_array[::-1]
print(reversed_array)

######### RESHAPIG ######

#### Use this array for the following practice:
myArray = np.array([[11,12,13], [14,15,16]])
# Reshape the array to have 3 rows
reshaped_array = myArray.reshape(3, -1)
print(reshaped_array)


############## Math ###########
####### use this array for the following practice:##########
myArray = np.arange(10)

# 1. Find the square of every number in the array
squared_array = np.square(myArray)
print("Square of every number:", squared_array)

# 2. Find the square root of every number in the array
sqrt_array = np.sqrt(myArray)
print("Square root of every number:", sqrt_array)

# 3. Multiply the square of each number with its respective square root
result_array = squared_array * sqrt_array
print("Result of multiplication:", result_array)

########## ADDING ELEMENTS ##########

####Use this array for the following practice:###########
myArray = np.array([[11,12,13], [14,15,16], [17,18,19]])

# 1. Add a new row of elements containing 20, 21, and 22
new_row = np.array([[20, 21, 22]])
myArray = np.vstack((myArray, new_row))

print("Array after adding a new row:")
print(myArray)

# 2. Add a new column of elements containing 30, 40, and 50
new_column = np.array([[30], [40], [50]])
# Check the shapes of arrays before stacking
print("Shape of myArray:", myArray.shape)
print("Shape of new_column:", new_column.shape)

# Transpose the new column if needed
if new_column.shape[1] == 1:
    new_column = new_column.T
# Attempt to stack arrays horizontally
try:
    myArray = np.hstack((myArray, new_column))
    print("\nArray after adding a new column:")
    print(myArray)
except Exception as e:
    print("Error during horizontal stacking:", e)

############# INSERTING ELEMENTS ###########
# 1. Add 1 column of 1 to this array: myArray = np.zeros((2,2))
myArray = np.zeros((2, 2))
myArray = np.hstack((myArray, np.ones((2, 1))))
print("Array after adding 1 column of 1:")
print(myArray)

# 2. Add 2 rows of 2 to the answer from part 1
additional_rows = np.zeros((2, myArray.shape[1]))
myArray = np.vstack((myArray, additional_rows))

print("\nArray after adding 2 rows of 2:")
print(myArray)

# 3. Remove the last column
myArray = myArray[:, :-1]

print("\nArray after removing the last column:")
print(myArray)

# 4. Remove the last row
myArray = myArray[:-1, :]

print("\nArray after removing the last row:")
print(myArray)

############## DELETING ITEMS##########3

# Define the array
myArray = np.matrix([[1, 2, 3], [4, 5, 6], [9, 8, 7]])

# Remove the middle column
myArray = np.delete(myArray, 1, axis=1)
print(myArray)
############ TEST EXERCISE #####

###Replace all odd numbers in the given array with -1
####Start with:exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
exercise_1[exercise_1 % 2 != 0] = -1
print(exercise_1)

#######Convert a 1-D array into a 2-D array with 3 rows########
##Start with: exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
exercise_2 = exercise_2.reshape(3, -1)
print(exercise_2)

###Add 202 to all the values in given array###
### Start with: exercise_3 = np.arange(4).reshape(2,-1)
exercise_3 = np.arange(4).reshape(2,-1)
exercise_3 += 202
print(exercise_3)

### Generate a 1-D array of 10 random integers. Each integer should be a number between 30 and 40 (inclusive)
exercise_4 = np.random.randint(30, 41, size=10)
print(exercise_4)

##Find the positions of:
##Elements in x where its value is more than its corresponding element in y, and
##Elements in x where its value is equals to its corresponding element in y.
x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])

more_than_y = np.where(x > y)[0]
equal_to_y = np.where(x == y)[0]
print(more_than_y, equal_to_y)

###Extract the first four columns of this 2-D array
#### Start with this:exercise_6 = np.arange(100).reshape(5,-1)

# Define the array
exercise_6 = np.arange(100).reshape(5, -1)

# Extract the first four columns
first_four_columns = exercise_6[:, :4]
print(first_four_columns)