import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))


# arr = np.array((1, 2, 3, 4, 5))
# print(arr)

# 0-D array
arr = np.array(12)
print(arr)

# 1-D array
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)

# 2-D array
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr)

# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# o'lchamlar sonini tekshirish
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Katta o'lchamdagi son
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

