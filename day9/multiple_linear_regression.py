# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model

m, n = list(map(int, (input().split())))
X = []
Y = []

for i in range(n):
    temp = list(map(float, (input().split())))
    x = temp[:-1]
    y = temp[-1]

    X.append(x)
    Y.append(y)

lm = linear_model.LinearRegression()
lm.fit(X, Y)

a = lm.intercept_
b = lm.coef_

p = int(input())
for i in range(p):
    test = list(map(float, (input().split())))
    pred = a + sum([coef*feature for coef,feature in zip(b,test)])
    print("{:.2f}".format(pred))

