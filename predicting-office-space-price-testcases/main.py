import os
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import preprocessing
from sklearn import decomposition
from matplotlib import pyplot as plt


if __name__ == '__main__':
    input_file = "input03.txt"
    output_file = "output03.txt"
    
    with open(input_file) as file:
        F, H = map(int, file.readline().split())
        x_data = []
        sales = []
        for i in range(H):
            line  = np.array(list(map(float, file.readline().split())))
            x_data.append(line[:-1])
            sales.append(line[-1])
            
        x_df = pd.DataFrame(x_data)
        n_test = int(file.readline())
        x_test = []
          
        for i in range(n_test):
            line = np.array(list(map(float, file.readline().split())))
            x_test.append(line)
    
    pca = decomposition.PCA(n_components=1)
    pca.fit(x_df)
    pca_data = pca.transform(x_df)
    
    plt.figure(figsize = (12, 7))
    plt.scatter(x = pca_data[:, 0], y = sales, color='red')
    # plt.show()
    
    poly_model = preprocessing.PolynomialFeatures(degree=5, include_bias=False)
    x_train = poly_model.fit_transform(x_df)
    x_test = poly_model.fit_transform(x_test)


    y_test = []
    with open(output_file) as file:
        for line in iter(file.readline, ''):
            y_test.append(float(line))
    
    model = linear_model.LinearRegression()
    model.fit(x_train, sales)
    
    y_pred = model.predict(x_test)
    
    # calculate score
    d = np.array([(abs(computed - expected) / expected) - 0.1 for computed, expected in zip(y_pred, y_test)])
    d_adjusted = max(max(d), 0)
    score = max(1 - d_adjusted, 0)
    print(score)
    
          
        

