# Air Quality Index (AQI) Exploratory Data Analysis

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Overview](#dataset-overview)
3. [Exploratory Data Analysis](#exploratory-data-analysis)
    - Data Quality Checks
    - Descriptive Statistics
    - Distribution Analysis
    - Outlier Detection
    - Correlation Analysis
    - Group-wise Analysis
    - Pollutant Contributions
4. [Conclusions](#conclusions)
5. [Visualizations](#visualizations)

---

## Introduction
Air pollution has a significant impact on public health and the environment. The **Air Quality Index (AQI)** is an essential metric used to represent the concentration of pollutants in the air. A higher AQI value represents more hazardous air quality. This project aims to conduct an exploratory data analysis (EDA) on global AQI data to understand the distribution of pollutants and identify trends and patterns in air quality across various cities and countries.

## Dataset Overview
The dataset contains the following columns:
- **Country**: Name of the country.
- **City**: City where the air quality was measured.
- **AQI Value**: The overall AQI index value.
- **CO AQI Value**: AQI value for Carbon Monoxide (CO).
- **Ozone AQI Value**: AQI value for Ozone (O3).
- **NO2 AQI Value**: AQI value for Nitrogen Dioxide (NO2).
- **PM2.5 AQI Value**: AQI value for Particulate Matter (PM2.5).
- **AQI Category**: Category based on AQI value (Good, Moderate, Unhealthy, etc.).

## Exploratory Data Analysis

### Data Quality Checks
The initial data quality checks involved:
- Checking for missing values and duplicates.
- Summary of the dataset, including key statistics.

### Descriptive Statistics
The AQI and pollutant data were summarized using statistical measures such as mean, median, minimum, maximum, and standard deviation. This helps understand the central tendencies and variability of air quality across the dataset.

### Distribution Analysis
- **AQI Value Distribution**: The histogram shows that most AQI values lie between 0 and 100, indicating moderate air quality in most regions.
- **CO AQI Value Distribution**: The concentration of CO in most locations is very low.
- **Ozone AQI Value Distribution**: Ozone levels are generally low, with most values falling below 50.
- **PM2.5 AQI Value Distribution**: PM2.5 concentrations have a wider range, indicating some regions with dangerously high levels of particulate matter.

### Outlier Detection
Boxplots were used to identify outliers in the AQI and pollutant values:
- Significant outliers were detected, especially in the CO and PM2.5 AQI values.
- These outliers represent locations with extreme pollution levels.

### Correlation Analysis
A correlation matrix was generated to analyze relationships between pollutants:
- **PM2.5** has the highest positive correlation with the overall AQI.
- **CO AQI** also shows a moderate correlation with the overall AQI.
- **Ozone AQI** has a weaker correlation with AQI compared to other pollutants.

### Group-wise Analysis
- The number of cities in each AQI category was analyzed. Most cities fall under the "Good" or "Moderate" AQI categories, with a small percentage of cities experiencing "Hazardous" air quality.
- The top 10 countries with the highest average AQI were visualized. South Korea shows the highest average AQI, followed by Bahrain and Mauritania.

### Pollutant Contributions
The mean AQI values for each pollutant were visualized:
- PM2.5 contributes the most to overall AQI, followed by Ozone and CO.

## Conclusions
The exploratory analysis reveals that:
- **PM2.5** is the major contributor to poor air quality globally, with high values in several regions.
- Most cities fall under the "Good" or "Moderate" AQI categories, but a few cities experience severely hazardous air quality.
- There is a strong correlation between **PM2.5** and overall AQI, making it a critical pollutant to monitor.

These findings emphasize the need for effective air quality management, especially in regions with high levels of particulate matter.

## Visualizations
Below are the key visualizations generated during the analysis:

### Distribution Plots
[AQI Distribution]![img.png](img.png)
[Boxplot for AQI and Pollutants]![img_1.png](img_1.png)

### Correlation Analysis
[Correlation Matrix]![img_3.png](img_3.png)
[Pairplot for AQI and Pollutants]
### Group-wise and Pollutant Contribution Analysis![img_2.png](img_2.png)
[AQI Categories by City]![img_4.png](img_4.png)
[Top 10 Countries with Highest AQI]![img_5.png](img_5.png)
[Mean Pollutant AQI Values]![img_6.png](img_6.png)
[AQI Categories Distribution]![img_7.png](img_7.png)
---

This README provides a comprehensive overview of the EDA performed on the AQI dataset and summarizes key insights from the analysis. The accompanying visualizations help illustrate the trends and patterns observed in the data.
