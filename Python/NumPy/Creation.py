import numpy as np

#We can create numpy arrays in different forms 1D,2D,3D
#array is a numpy function we use for the creation of array here are creating 1D numpy array
arr1=np.array([1,2,3,4,5])
print(arr1)
print(arr1.ndim)
#2D ARRAY
arr2=np.array([
    [1,2,3],[4,5,6]
    ])
print(arr2)
print(arr2.ndim)
#3D ARRAY
arr3=np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
    ])
print(arr3)
print(arr3.ndim)
#Creating Numpy array using the inbuilt functions
#By using the arange()
range=np.arange(1,11)
print(range)
#By using the linspace
a=np.linspace(1,10,10)
print(a)
b=np.ones([2,3])
print(b)