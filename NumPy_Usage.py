import numpy as np


def arithmetic_operations():
    a = np.array([(2, 3, 4, 5, 1),
                  (8, 3, 9, 7, 0)])
    print("Original Array A:\n", a)

    # Multiply the array by 2
    print("Multiply array by 2:\n", 2 * a)
    # Divide the array by 2
    print("Divide array by 2:\n", a / 2)

    b = np.array([(100, 200, 300, 400, 500),
                  (10, 20, 30, 40, 50)])
    print("Original Array B:\n", b)

    ### The shapes of Array A and Array B
    ### must be the same for the below calculations
    # Adding two arrays
    print("Array A + Array B:\n", a + b)
    # Multiplying Array A by Array B
    print("Array A * Array B:\n", a * b)
    # Dividing Array A by Array B
    print("Array A / Array B:\n", a / b)


def masking_boolean_arrays():
    a = np.array([(20, 25, 10, 34, 25, 22, 34, 32),
                  (23, 42, 12, 2, 23, 32, 12, 11)])
    print("Original Array:\n", a)
    # size is the number of elements
    # shape is the number of rows by number of columns
    print("Size of array: ", a.size,
          "\nShape of array: ", a.shape)

    mean = a.mean()
    print("Mean of array: ", mean)

    ### Masking
    # Prints all elements that are less than the mean
    print("Elements less than mean:\n", a[a < mean])
    # Replace all elements that are less than the
    # mean with the mean value.
    a[a < mean] = mean
    print("Replacing elements by masking:\n", a)


def indexing_arrays():

    a = np.random.rand(5)
    print(a)

    # Accessing elements in an array by using
    # another array whose elements will be the indices
    indices = np.array([1, 1, 2, 3])
    print(a[indices])


def modifying_array_elements():
    a = np.random.randint(0, 10, (5, 4), dtype=np.int32)
    print("Original Array:\n", a)

    # Setting the value of an element by index
    a[0, 0] = 20
    print("Updating first element:\n", a)

    # Setting the value for the elements in a specified column
    a[:, 3] = 40
    print("Updating all rows in column 3:\n", a)
    # Setting the value for the elements in a specified row
    a[2, :] = 60
    print("Updating all columns in row 2:\n", a)


def accessing_array_elements():

    a = np.random.rand(5, 4)
    print("Array:\n", a)

    # Locate the element on row 2 column 3
    element = a[2, 3]
    print("Element in position [2, 3]:\n", element)

    # Obtain the elements in row 0 which are in column 1 and 2
    group_of_elements = a[0, 1:3]
    print("Middle two elements first row:\n", group_of_elements)

    # Top left elements in the array
    top_left_elements = a[0:2, 0:2]
    print("Top left elements:\n", top_left_elements)

    ### Slicing with stepping over values
    # The below will select columns 0 and 2 for every row
    stepping_elements_all_rows = a[:, 0:3:2]
    print("Stepping over every other column:\n", stepping_elements_all_rows)
    # The below will select rows 0 2 4 for every column
    stepping_elements_all_columns = a[0:6:2, :]
    print("Stepping over every other row:\n", stepping_elements_all_columns)


def locate_max_value_array():
    a = np.array([9, 3, 2, 14, 23, 43, 1, 0, 2, 43], dtype=np.int32)
    print("Array:\n", a)

    # Locate the max element and its index
    print("Maximum element: ", a.max())
    # Obtains the index of the max element
    ### argmax only returns the first occurance of the max value
    print("Index of max element: ", a.argmax())


def operations_on_ndarray():

    # The seed attribute is used to maintain that the same random
    # numbers are generated.
    np.random.seed(693)
    # Creates an array of 5 Rows and 4 Columns which has 20 elements
    # Each element is an integer between 0 an 10
    a = np.random.randint(0, 10, size=(5, 4))
    print("Array:\n", a)

    # Prints the sum of all the elements in the array
    print("Sum of all elements: ", a.sum())
    # Sums the elements of each column
    print("Sum of each column:\n", a.sum(axis=0))
    # Sums the elements of each row
    print("Sum of each row:\n", a.sum(axis=1))

    ### Calculating min, max and mean of an array an its elements
    # Calculating the min of an array
    print("Minimum of array:\n", a.min())
    # Calculating the min of the rows
    print("Minimum of rows in array:\n", a.min(axis=1))
    # Calculating the max of the columns
    print("Maximum of columns in array:\n", a.max(axis=0))
    # Calculating the mean of an array
    print("Mean of an array:\n", a.mean())


def create_arrays_with_random_numbers():

    ### randint only selects integer values

    # An array of one element between 0 and 10
    print(np.random.randint(10))
    # An array of one element between 0 and 10.
    # The high and low boundaries are stated
    print(np.random.randint(0, 10))
    # An one dimensional array of 5 elements. Each element
    # is a random integer between 0 and 10
    print(np.random.randint(0, 10, size=5))
    # A two dimensional array stated by the size parameter
    # Each element is a random integer between 0 and 10
    print(np.random.randint(0, 10, size=(2, 3)))


def array_attributes():
    # Generates an array with 5 rows and 4 columns
    # filled with random floating point numbers between
    # 0.0 and 1.0
    a = np.random.random((5, 4))

    # Prints array
    print(a)
    # Prints shape of array. Tuple of (Row, Column)
    print(a.shape)
    # Prints number of rows in array
    print(a.shape[0])
    # Prints number of columns in array
    print(a.shape[1])
    # Prints the number of elements in an array
    print(a.size)
    # Prints the dtype of the elements of the array
    print(a.dtype)


def basic_array_creation():

    ### NOTES ###
    # ndarray means a n dimensional array

    # Creating an empty array loads the array elements with whatever data
    # is in the current memory location. Pretty cool!

    # List of tuples
    n_dimensional_array_tuple = np.array([(2, 3, 4), (5, 6, 7)])

    # List of lists
    n_dimensional_array_list = np.array([[10, 11, 12], [13, 14, 15]])

    print(n_dimensional_array_list)
    print(n_dimensional_array_tuple)

    # Creating an array with pre-populated data(number ones below)
    # The below object takes in a tuple which represents the
    # dimensions of array. Format: (Rows, Column)
    # dtype is called to state the type of numerical value
    # that the array should use.
    print(np.ones((5, 4), dtype=np.int_))


if __name__ == "__main__":
    basic_array_creation()
    #create_arrays_with_random_numbers()
    #array_attributes()
    #operations_on_ndarray()
    #locate_max_value_array()
    #accessing_array_elements()
    #modifying_array_elements()
    #indexing_arrays()
    #masking_boolean_arrays()
    #arithmetic_operations()
