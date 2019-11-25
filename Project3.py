import pandas as pd

dataset = pd.read_csv('/home/akshay.kumar/machine_learning/Regression/02Students.csv')
df = dataset.copy()

X = df.iloc[:, :-1]
Y = df.iloc[:,-1]

#Split for rows

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1234)

#Training Our Model Simple Linear Regression

from sklearn.linear_model import LinearRegression
std_reg = LinearRegression()

# Provide the training Data to make std_reg to train
std_reg.fit(x_train, y_train)

#Now let's do some prediction
y_predict = std_reg.predict(x_test)

# Get the R-square
mlr_score = std_reg.score(x_test, y_test)

# Coefficient and Intercept
mlr_coefficient = std_reg.coef_
mlr_intercept = std_reg.intercept_

# Equation of the line
# y = 1.31 + 4.67 &* Hours + 5.1 * SHours
#calculate the errors using RMSE
from sklearn.metrics import mean_squared_error
import math

mlr_mse = math.sqrt(mean_squared_error(y_test, y_predict))

import matplotlib.pyplot as plt
plt.scatter(x_test, y_test)
plt.plot(x_test, y_predict)
plt.ylim(ymin = 0)
plt.show()
