# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:51:53 2019

@author: akshay.kumar
"""

import matplotlib.pyplot as plt

#Line Chart
x_days = [1,2,3,4,5]
y_price1 = [9,9.5,10.2,10,12]
y_price2 = [11,12,10.5,11.5,12.5]

plt.title("Stock Movement")
plt.xlabel("Week Days")
plt.ylabel("Price in USD")

plt.plot(x_days, y_price1, label="Stock1")
plt.plot(x_days, y_price2, label="Stock2")
plt.legend(loc = 2, fontsize=12)
plt.show()


#Bar Chart

import matplotlib.pyplot as plt 
x_cities = ['Delhi', 'Haryana', 'Uttar Pradesh', 'Punjab']
y_temp = [75, 65, 105, 98]

plt.title("Temperature Variation")
plt.xlabel("Cities")
plt.ylabel("Temperature")

plt.bar(x_cities, y_temp)

plt.show()

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()


# Histogram

f = open('agedata.csv', 'r')
agefile = f.readlines()
age_list = []

for records in agefile:
    age_list.append(int(records))
    
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.title("Age Histogram")
plt.xlabel("Group")
plt.ylabel("Age")

plt.hist(age_list, bins, histtype='bar', rwidth = 0.9)

plt.show()


# BoxPlot

f = open('agedata.csv', 'r')
salesfile = f.readlines()
sales_file = []

for records in salesfile:
    sales_file.append(int(records))
plt.title("Box Plot of Sales")
plt.boxplot(sales_file)
plt.show()



#Pie Chart
import matplotlib.pyplot as plt;
f = open('citydata.csv', 'r')
city_name = f.readlines()


city_list = [];
for records in city_name:
    age, city = records.split(sep=',')
    city_list.append(city)

from collections import Counter

city_count = Counter(city_list)

city_names = list(city_count.keys())
city_values = list(city_count.values())
plt.subplot(2,1,1)
plt.pie(city_values, labels=city_names, autopct='%.2f%%')
plt.show()




#Scatter Plot
import matplotlib.pyplot as plt
f= open('salesdata.csv','r')
salefile = f.readlines()

s_list = []
c_list = []

for records in salefile:
    sale, cost = records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))
plt.subplot(2,1,2)  
plt.title("Sales Vs Cost")
plt.xlabel("Sale")
plt.ylabel("Cost")

plt.scatter(s_list, c_list)
plt.tight_layout()
plt.show()




























