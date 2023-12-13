# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:38:33 2023

@author: 786
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\786\Desktop\Urban_Population(2).csv'
data = pd.read_csv(file_path)

# Select data for the specific indicators and country
indicators_to_plot = ['Urban population', 'CO2 emissions (kt)']
selected_country = 'Switzerland'

# Filter data
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(indicators_to_plot))]

# Extract years and values for the bar chart
years = selected_data.columns[2:]
values1 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[0]].iloc[0, 2:]
values2 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[1]].iloc[0, 2:]

# Plot the clustered column chart
plt.figure(figsize=(12, 8))
bar_width = 0.35
bar_positions1 = [pos - bar_width/2 for pos in range(len(years))]
bar_positions2 = [pos + bar_width/2 for pos in range(len(years))]

bar1 = plt.bar(bar_positions1, values1, width=bar_width, label=indicators_to_plot[0], color='Blue')
bar2 = plt.bar(bar_positions2, values2, width=bar_width, label=indicators_to_plot[1], color='Orange')

plt.title(f'{selected_country} - Urban Population and CO2 Emissions (kt) (2000-2020)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.xticks(range(len(years)), years)  # Set the x-axis ticks to represent years
plt.legend()
plt.grid(axis='y')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Replace this with the actual path to your CSV file
file_path = r'C:\Users\786\Desktop\Urban_Population(2).csv'
data = pd.read_csv(file_path)

# Select countries and indicators of interest
selected_countries = ['Australia', 'United Arab Emirates', 'Brazil', 'Canada', 'Switzerland', 'Germany', 'India', 'Japan', 'United States']
selected_indicators = ['CO2 emissions (kt)']

# Filter data for selected countries and indicators
selected_data = data[(data['Country Name'].isin(selected_countries)) & (data['Indicator Name'].isin(selected_indicators))]

# Set up bar positions and width
bar_positions = range(len(selected_countries))
bar_width = 0.35

# Create subplots
fig, ax = plt.subplots()

# Plot bars for each indicator and country
for i, indicator in enumerate(selected_indicators):
    for j, country in enumerate(selected_countries):
        subset_data = selected_data[(selected_data['Country Name'] == country) & (selected_data['Indicator Name'] == indicator)]
        ax.bar(bar_positions[j] + i * bar_width, subset_data.iloc[0, 2:], width=bar_width, label=f'{country} - {indicator}')

# Set labels and title
ax.set_xticks([pos + bar_width / 2 for pos in bar_positions])
ax.set_xticklabels(selected_countries)
ax.set_xlabel('Country')
ax.set_ylabel('Indicator Value')
ax.set_title('Bar Chart for Selected Indicators and Countries')

# Add legend
ax.legend()

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\786\Desktop\Urban_Population(2).csv'
data = pd.read_csv(file_path)

# Select specific indicator for analysis
selected_indicator = 'Urban population'

# Select the specific countries for analysis
selected_countries = ['Australia', 'United Arab Emirates', 'Brazil', 'Canada', 'Switzerland', 'Germany', 'India', 'Japan', 'United States']

# Filter data for selected indicator and countries
selected_data = data[(data['Indicator Name'] == selected_indicator) & (data['Country Name'].isin(selected_countries))]

# Plot time trends for the selected indicator and countries
plt.figure(figsize=(16, 10))
for country in selected_countries:
    country_data = selected_data[selected_data['Country Name'] == country]
    
    # Check if there is data for the country before plotting
    if not country_data.empty:
        plt.plot(country_data.columns[2:], country_data.iloc[0, 2:], label=country)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title(f'Time Trends for {selected_indicator} Across Countries')
plt.legend()

# The y-axis limits are determined automatically

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\786\Desktop\Urban_Population(2).csv'
data = pd.read_csv(file_path)

# Select specific indicator for analysis
selected_indicator = 'CO2 emissions (kt)'

# Select the specific countries for analysis
selected_countries = ['Australia', 'United Arab Emirates', 'Brazil', 'Canada', 'Switzerland', 'Germany', 'India', 'Japan', 'United States']

# Filter data for selected indicator and countries
selected_data = data[(data['Indicator Name'] == selected_indicator) & (data['Country Name'].isin(selected_countries))]

# Scatter plot for the selected indicator and countries
plt.figure(figsize=(12, 8))

for country in selected_countries:
    country_data = selected_data[selected_data['Country Name'] == country]
    
    # Check if there is data for the country before plotting
    if not country_data.empty:
        plt.scatter(country_data.columns[2:], country_data.iloc[0, 2:], label=country)

plt.xlabel('Year')
plt.ylabel(f'{selected_indicator} Value')
plt.title(f'Scatter Plot for {selected_indicator} Across Countries')
plt.legend()
plt.grid(True)
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\786\Desktop\Urban_Population(2).csv'
data = pd.read_csv(file_path)

# Select specific indicators for correlation matrix
selected_indicators = ['Urban population', 'CO2 emissions (kt)']

# Choose a specific country
selected_country = 'China'

# Filter data for selected indicators and country
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(selected_indicators))]

# Extract years dynamically from the columns
years = selected_data.columns[2:]  # Assuming the years start from the 3rd column

# Pivot the data
pivot_data = selected_data.melt(id_vars=['Country Name', 'Indicator Name'], value_vars=years, var_name='Year', value_name='Value')
pivot_data['Year'] = pivot_data['Year'].astype(int)  # Convert 'Year' to integer type

# Create a correlation matrix for selected indicators
correlation_matrix = pivot_data.pivot_table(index='Year', columns='Indicator Name', values='Value').corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Set the title
plt.title(f'Correlation Matrix for {selected_country} - Selected Indicators')

# Show the plot
plt.show()




