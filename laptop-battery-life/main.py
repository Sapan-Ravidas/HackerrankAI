x = []
y = []
data = open('trainingdata.txt')
for line in data:
    xi, yi = map(float, line.split(','))
    if (xi < 4):
        x.append(xi)
        y.append(yi)
data.close()

n = len(x)
x_avg = sum(x) / n
y_avg = sum(y) / n

numerator = 0
denominator = 0
for i in range(n):
    x_diff = x[i] - x_avg
    numerator += x_diff * (y[i] - y_avg)
    denominator += x_diff ** 2
b = (1.0 * numerator) / denominator
a = y_avg - b * x_avg

print(a, b)
q = float(input())
if (q < 4):
    print( "%.2f" % (a + b * q))
else:
    print(8.00)
