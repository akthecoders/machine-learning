import pandas as pd
import matplotlib.pyplot as plt

f = pd.read_csv('/home/akshay.kumar/machine_learning/Regression/corr.csv')


f['t0'] = pd.to_numeric(f['t0'], downcast = "float")
plt.acorr(f['t0'], maxlags = 10)

#Create TimeLog dataset using panda shift function
t_1 = f['t0'].shift(+1).to_frame()
t_2 = f['t0'].shift(+2).to_frame()