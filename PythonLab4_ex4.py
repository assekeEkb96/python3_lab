a = [1,2,2,2,4,4,5,6,12,100]
res_array = [a[i] for i in range(len(a)) if a.count(a[i]) == 1]
print(res_array)
