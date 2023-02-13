x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
result = 8

for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] + x[j] == result:
            print(x[i], x[j])
