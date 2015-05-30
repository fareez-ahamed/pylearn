
# This program does the Linear Regression on a subset Flat Resales data
# taken from data.gov.sg. We consider only two fields here for simple
# regression. The fields taken are floor space (in sqft/sqm) & price
#
# This problem is solved using SciPy

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

# Read the data into a DataFrame using Pandas
data = pd.read_excel('data/bedok.xlsx')

# Convert the needed columns in the dataframe
# to numpy array
x = data["floor"].as_matrix()
y = data["price"].as_matrix()

# Calculate Linear progression using SciPy 
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print "Slope:", slope
print "Intercept", intercept

# Plot the data points
plt.plot(data["floor"].tolist(), data["price"].tolist(), 'ro')

# Plot the line coords we calculated using slope & intercept
plt.plot(x, slope * x + intercept, color='blue',
        linewidth=3)

# Display the plot
plt.show()