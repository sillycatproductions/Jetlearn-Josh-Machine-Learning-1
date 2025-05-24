x = [10,20,30,40,50]
y = [600,700,800,900,1000]

def findMean(a):
    return sum(a)/len(a)

meanx = findMean(x)
meany = findMean(y)

print(meanx)
print(meany)

numer = 0
denom = 0

for i in range(len(x)): 
    numer = numer + ((x[i] - meanx) * (y[i] - meany)) 
    denom = denom + pow((x[i] - meanx), 2) 

m = numer / denom
print('m =', m)

c = round(meany - m * meanx,1)
print('c =', c)


import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[10], [20], [30], [40], [50]]) 
y = np.array([[600], [700], [800], [900], [1000]]) 

reg = LinearRegression().fit(x,y) 

print('m =', reg.coef_) 
print('c =', reg.intercept_) 