# y = mx + c [y,x = variable | m = slope | c = intercept]
# m = sum((xi - mean(x)) * (yi-mean(y)) / sum((xi - mean(x)) ^ 2)
# c = mean(y) - m * mean(x)

# [yp = prediction | ya = actual answer | e = error] e = yp - ya
# line that gives minimum RMSE [RMSE = Root Mean Squared Error] is the best fit line

x = [1,2,3,4,5]
y = [6,7,8,9,10]

def findMean(a):
    return sum(a)/len(a)

meanx = findMean(x)
meany = findMean(y)

print(meanx)
print(meany)

#calculate m
numer = 0
denom = 0

for i in range(len(x)): 
    numer = numer + ((x[i] - meanx) * (y[i] - meany)) #numer = numerator
    denom = denom + pow((x[i] - meanx), 2) #denom = denominator

m = numer / denom #fraction
print('m =', m)

#calculate c
c = round(meany - m * meanx,1)
print('c =', c)

#find m and c using machine learning algorithm
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4], [5]]) #make array with numpy
y = np.array([[6], [7], [8], [9], [10]]) #wawawa

reg = LinearRegression().fit(x,y) #initialises model (LinearRegression)

print('m =', reg.coef_) #coef_ = co efficient (m)
print('c =', reg.intercept_) #intercept_ = intercept (c)
