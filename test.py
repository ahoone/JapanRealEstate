import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


name_df = "/Users/noahbensoussen/Desktop/AD/data.csv"

#df = pd.read_csv(name_df)

df = pd.read_csv(name_df, skiprows=range(0, 0), nrows=100000)


#df = df.loc[:,"BuildingYear"]

#print(df)

count = df.groupby("BuildingYear").count()

count=count.loc[:,"Prefecture"]

date = []
num = []
o = 1945
for i in count :
	date.append(o)
	o=o+1
	num.append(i)

#print(count.loc(axis=0)[:,"Prefecture"])

plt.plot(date,num)
plt.show()