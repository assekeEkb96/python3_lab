from functools import reduce
array = [i for i in range(100,1001,2)]
multi_all = reduce(lambda x,y: x*y, array)
print(multi_all)
