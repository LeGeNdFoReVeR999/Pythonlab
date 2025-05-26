import numpy as np

array1=np.array([1,2,3,4,5])

zeros_arrays=np.zeros((2,3))

ones_array=np.ones((2,3))

identity_array=np.eye(3)

random_array=np.random.rand(2,2)

range_array=np.arange(2,12,4)

eq_sp_array=np.linspace(0,10,5)

print("array from list:\n",array1)
print("\n array of zeros:\n",zeros_arrays)
print("\nIdentity array:\n",identity_array)
print("\nArray of random values\n",random_array)
print("\narray in a range\n",range_array)
print("\narray with equally spaced elements:\n",eq_sp_array)
print("\nShape of a random array :",random_array.shape)
print("\nData type of the array:",random_array.dtype)

a=np.arange(10)
print("\nOriginal array:\n",a)

b=a.reshape(2,5)
print("\nReshaped array:\n",b)

c=a[0:5]
print("\nSlice of original array:\n",c)

d=b[0,2:]
print("\nSlice of reshaped array:\n",d)

avg=np.mean(a)
max_a=np.max(a)
min_a=np.min(a)

print(f"\n The averae of original array:{avg}\nThe maximum of original array:{max_a}\nThe minimum of original array:{min_a}\n")

e=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Original array:\n",e)
e[0,1]=99
e[:2]=[100,200,300]
print("Modified array:\n",e)
