import datasets
import regression

X,Y = datasets.load_liner_example1()

print(X)

print(X[0])

print(Y)

#ver.1
model = regression.LunerRegression()

model.x