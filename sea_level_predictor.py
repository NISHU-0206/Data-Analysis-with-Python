import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# Create first line of best fit for all data
slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
line_all = intercept_all + slope_all * years_extended
plt.plot(years_extended, line_all, color='red', label='Best Fit Line (1880-2050)')

# Create second line of best fit using data from 2000
df_2000 = df[df['Year'] >= 2000]
slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
years_2000 = pd.Series(range(2000, 2051))
line_2000 = intercept_2000 + slope_2000 * years_2000
plt.plot(years_2000, line_2000, color='green', label='Best Fit Line (2000-2050)')

# Customize the plot
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.legend()
plt.grid(True)

plt.savefig('sea_level_plot.png')
plt.show()
