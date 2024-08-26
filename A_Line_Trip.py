def minimum_tank_size(x, stations):
    stations = [0] + stations + [x]
    max_gap = 0
    for i in range(len(stations) - 1):
        temp_gap = stations[i+1] - stations[i]
        if stations[i+1] == stations[-1]:
            temp_gap += temp_gap
            max_gap = max(max_gap, temp_gap)
            break
        else:
            if temp_gap > max_gap:
                max_gap = temp_gap
    
    for i in range(len(stations) - 1, 0, -1):
        temp_gap = stations[i] - stations[i-1]
        if temp_gap > max_gap:
            max_gap = temp_gap
    
    return max_gap



t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    stations=list(map(int,input().split()))
    print(minimum_tank_size(x, stations))

