array = [300,2,12,44,1,1,4,10,7,1,78,123,55]

def greater_previous(array):
    res = (array[i] for i in range(1,len(array)) if array[i]>array[i-1])
    return [i for i in res]
print(greater_previous(array))

