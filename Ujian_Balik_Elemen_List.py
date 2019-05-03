def balikposisi(x):
    y = []
    for i in range(len(x)-1, -1, -1):
        y.append(x[i])
    return y

x =[1, 2, 3, 4, 5]
y =['a', 'b', 'c', 'd']

print(balikposisi(x))
print(balikposisi(y))