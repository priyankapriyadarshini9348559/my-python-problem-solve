# Create a 1D NumPy array of numbers from 1 to 30.
import numpy as np
arr=np.arange(1,31)
print(arr)
print("______________________________________________")
# Create a 1D array of even numbers between 2 and 40.
import numpy as np
arr1=np.arange(2,41,2)
print(arr1)
print("______________________________________________")
#Create a 2D array of shape (3, 3) filled with all zeros.
import numpy as np
arr_2d=np.zeros((3,3),dtype=int)
print(arr_2d)
print("______________________________________________")
# Create a 2D array of shape (4, 4) filled with random integers between 1 and 100.
arr_2d1=np.random.randint(1,101, size=(4,4))
print(arr_2d1)
print("______________________________________________")
# Extract the first column of a 2D array.
arr_2D=np.array([[2,3,4],
                 [4,7,6],
                 [8,9,10]])
first_col=arr_2D[ :,0]
print(first_col)
print("______________________________________________")
# Reverse a NumPy array using slicing.
arr3=np.array([56,78,74,39])
resverse_array=arr3[::-1]
print(resverse_array)