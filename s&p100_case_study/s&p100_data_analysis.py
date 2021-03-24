from typing import Any, Union

import pandas as pd
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Examine the lists
# Reading the file and exploring the data set

df: Union[Union[TextFileReader, Series, DataFrame, None], Any] = pd.read_csv('sector.csv')
print(df.columns)
print(df.head())
print(df.shape)

# Defining lists
names, prices, earnings, sectors = df['Name'], df['Price'], df['EPS'], df['Sector']

# Filtering the first four items of names
print(names[0:4])

# Filtering information on the last company in the dataset
print(names[101])
print(prices[101])
print(earnings[101])
print(sectors[101])

# Step 2: Convert lists to arrays and perform array operations
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Calculating P/E ratio
pe = (prices_array / earnings_array)
print(pe)

# Filtering arrays by sector Information Technology
boolean_array = (sectors == 'Information Technology')
it_names = names[boolean_array]
it_pe = pe[boolean_array]
print(it_names)
print(it_pe)

# Filtering arrays by sector Consumer Staples
boolean_array = (sectors == 'Consumer Staples')
cs_names = names[boolean_array]
cs_pe = pe[boolean_array]
print(cs_names)
print(cs_pe)

# Summarizing sector data for IT and Consumer Staples
it_pe_mean = np.mean(it_pe)
it_pe_std = np.std(it_pe)
print(it_pe_mean)
print(it_pe_std)
cs_pe_mean = np.mean(cs_pe)
cs_pe_std = np.std(cs_pe)
print(cs_pe_mean)
print(cs_pe_std)

# Step3: Visualizations
# Plot P/E ratios -  using a scatter plot for each company in these two sectors
plt.scatter(it_names, it_pe, color='red', label='IT')
plt.scatter(cs_names, cs_pe, color='green', label='CS')
plt.legend()
plt.xlabel('Company ID')
plt.ylabel('P/E Ratio')
plt.figtext(0.5, 0.01, 'From the above plot we can see that there is an outlier corresponding to the IT sector.',
            fontsize=9.5, ha="center",va="center")
plt.savefig("sectors_scatterplot_snapshot.jpg")
plt.show()

# Histogram of P/E ratios - To visualize and understand the distribution of the P/E ratios in the IT Sector
plt.hist(x=it_pe, bins=8)
plt.xlabel('P/E ratio')
plt.ylabel('Frequency')
plt.figtext(0.5, 0.01, "From the above histogram we observe that there is a stock (outlier) with P/E ratio > 50",
            fontsize=9.5, ha='center',va="center")
plt.savefig("ITsector_hist_snapshot.jpg")
plt.show()

# Identifying the name of the company (outlier)
outlier_price = it_pe[it_pe > 50]
outlier_name = it_names[it_pe > 50]
print(outlier_name)
print("In 2017," + str(outlier_name) + "had an abnormally high P/E ratio of" + str(round(outlier_price[0], 2)) + ".")
