import statistics
from scipy import stats


# 25017.0 62784.2

if __name__ == '__main__':
    with open("input/input00.txt") as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
        
        mean = statistics.mean(arr)
        print(mean)
        
        median = statistics.median(arr)
        print(median)
        
        mode = stats.mode(arr)[0][0]
        print(mode)
        
        xdiff = 0
        for a in arr:
            xdiff += (a - mean) ** 2
        std = round(pow(xdiff / n, 0.5), 1)
        print(std)
        
        z = 1.96
        SE = std / (n ** 0.5)
        x1 = round(mean - (z * SE), 1)
        x2 = round(mean + (z * SE), 1)
        print(x1, x2)
        
        
    