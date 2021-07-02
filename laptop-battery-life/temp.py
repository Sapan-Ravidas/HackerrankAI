
if __name__ == '__main__':
    timeCharged = float(input().strip())
    
    x_data = []
    y_data = []
    with open("trainingdata.txt") as file:
        for line in iter(file.readline, ''):
            x, y = map(float, line.split(','))
            if x < 4:
                x_data.append(x)
                y_data.append(y)
        
    covar = 0
    covarx = 0
    N = len(x_data)
    x_mean = sum(x_data) / N
    y_mean = sum(y_data) / N
    
    for i in range(len(x_data)):
        x_diff = x_data[i] - x_mean
        y_diff = y_data[i] - y_mean
        covar += x_diff * y_diff
        covarx += x_diff * x_diff
    
    slope = covar / covarx
    intercept = y_mean - slope * x_mean
    
    
    if timeCharged > 4:
        print(8.00)
    else:
        print("{0:0.02f}".format(intercept + slope * timeCharged))
