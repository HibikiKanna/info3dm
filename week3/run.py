import datasets
import regression
import importlib

X,Y = datasets.load_liner_example1()

print(X)

print(X[0])

print(Y)

#ver.1
model = regression.LunerRegression()

model.x

#ver.2
importlib.reload(regression)
model = regression.LunerRegression()
model.fit(X,Y)
print(model.theta)