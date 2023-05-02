def inputDic():
    n = int(input('Nhập n: '))
    a = {}
    for i in range(1, n + 1):
        a[i] = i ** 2
    return n, a


a, my_dict = inputDic()
print(my_dict)
