# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'global_air_pollution_dataset.csv'
df = pd.read_csv(file_path)

# Checking for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Checking for duplicates
print("\nNumber of duplicate rows:", df.duplicated().sum())

# Dropping duplicate rows (if necessary)
df_cleaned = df.drop_duplicates()
# Descriptive statistics for numeric columns
desc_stats = df_cleaned.describe()
print("\nDescriptive Statistics:\n", desc_stats)
# Plotting distributions of AQI and pollutant values
plt.figure(figsize=(15,10))

# AQI Value Distribution
plt.subplot(2, 2, 1)
sns.histplot(df_cleaned['AQI Value'], bins=30, kde=True)
plt.title('Distribution of AQI Values')

# CO AQI Value Distribution
plt.subplot(2, 2, 2)
sns.histplot(df_cleaned['CO AQI Value'], bins=30, kde=True)
plt.title('Distribution of CO AQI Values')

# Ozone AQI Value Distribution
plt.subplot(2, 2, 3)
sns.histplot(df_cleaned['Ozone AQI Value'], bins=30, kde=True)
plt.title('Distribution of Ozone AQI Values')

# PM2.5 AQI Value Distribution
plt.subplot(2, 2, 4)
sns.histplot(df_cleaned['PM2.5 AQI Value'], bins=30, kde=True)
plt.title('Distribution of PM2.5 AQI Values')

plt.tight_layout()
plt.show()
# Outlier Detection with Boxplots
plt.figure(figsize=(15,10))

# Boxplot for AQI Value
plt.subplot(2, 2, 1)
sns.boxplot(x=df_cleaned['AQI Value'])
plt.title('Boxplot for AQI Value')

# Boxplot for CO AQI Value
plt.subplot(2, 2, 2)
sns.boxplot(x=df_cleaned['CO AQI Value'])
plt.title('Boxplot for CO AQI Value')

# Boxplot for Ozone AQI Value
plt.subplot(2, 2, 3)
sns.boxplot(x=df_cleaned['Ozone AQI Value'])
plt.title('Boxplot for Ozone AQI Value')

# Boxplot for PM2.5 AQI Value
plt.subplot(2, 2, 4)
sns.boxplot(x=df_cleaned['PM2.5 AQI Value'])
plt.title('Boxplot for PM2.5 AQI Value')

plt.tight_layout()
plt.show()
# Correlation matrix for AQI and pollutant values
correlation_matrix = df_cleaned[['AQI Value', 'CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of AQI and Pollutants')
plt.show()

# Pairplot to visualize relationships
sns.pairplot(df_cleaned[['AQI Value', 'CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']])
plt.show()
# Grouping data by AQI Category and getting the count of cities in each category
aqi_category_counts = df_cleaned.groupby('AQI Category')['City'].count()

# Bar Plot for AQI Categories
plt.figure(figsize=(10, 6))
aqi_category_counts.plot(kind='bar')
plt.title('Number of Cities in Each AQI Category')
plt.xlabel('AQI Category')
plt.ylabel('Number of Cities')
plt.show()

# Grouping by Country and calculating the average AQI per country
avg_aqi_per_country = df_cleaned.groupby('Country')['AQI Value'].mean().sort_values(ascending=False)

# Bar Plot for top 10 countries with highest average AQI
plt.figure(figsize=(12, 6))
avg_aqi_per_country.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries with Highest Average AQI')
plt.ylabel('Average AQI')
plt.xlabel('Country')
plt.show()
# Bar plot to show mean AQI values for each pollutant
mean_pollutant_aqi = df_cleaned[['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']].mean()

plt.figure(figsize=(10, 6))
mean_pollutant_aqi.plot(kind='bar', color='green')
plt.title('Mean AQI Values for Pollutants')
plt.ylabel('Mean AQI Value')
plt.xlabel('Pollutant Type')
plt.show()

# Pie chart for AQI Categories distribution
aqi_category_pie = df_cleaned['AQI Category'].value_counts()

plt.figure(figsize=(8, 8))
aqi_category_pie.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3')
plt.title('AQI Categories Distribution')
plt.ylabel('')
plt.show()
