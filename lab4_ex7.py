def fact(n):
    tmp = 1
    for i in range(1,n+1):
        tmp = tmp*i
        yield tmp

n = int(input('Enter n: '))

for i in fact(n):
    print(i)