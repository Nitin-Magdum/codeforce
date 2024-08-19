t = int(input())
for i in range(t):
    data = input()
    if len(data) <= 10:
        print(data)
    else:
        print(data[0] + str(len(data)-2) + data[-1])
