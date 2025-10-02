import pandas as pd, numpy as np

Print ("Hello professor")
df = pd.read_csv("iris.csv")
x = df['sepal.length'].to_numpy()
y = df['sepal.width'].to_numpy()
m, b = np.polyfit(x, y, 1)
yhat = m*x + b
r2 = 1 - ((y - yhat)**2).sum()/((y - y.mean())**2).sum()

print(f"MODEL: sepal.width ~ sepal.length")
print(f"slope={m:.6f}  intercept={b:.6f}  R2={r2:.6f}")
