import numpy as np

print('Hello World')
print(1+1)


sample1 = np.array([0,1,2])
print(sample1)
a = np.array([2,4,5,6])
a = a+1
print(a)


l_2d = [[0, 1, 2], [3, 4, 5]]
print(l_2d)


print([list(x) for x in list(zip(*l_2d))])

b = np.asarray([[1,2,3],[4,5,6]])
print(3*b)
c = np.asarray([[2,3,4],[5,6,7]])
print(b*c)

arr = np.random.rand(100)
print(np.mean(arr))