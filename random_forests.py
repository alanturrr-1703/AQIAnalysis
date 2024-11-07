# Re-importing necessary libraries due to kernel reset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
# Importing necessary libraries for visualization
import matplotlib.pyplot as plt
import seaborn as sns
# Loading the dataset
file_path = 'global_air_pollution_dataset.csv'
df = pd.read_csv(file_path)

# Handling categorical variables and missing data
# Dropping rows with missing target values
df = df.dropna(subset=['AQI Value'])

# Encoding categorical variables if present
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Separating features and target variable
X = df.drop(columns=['AQI Value'])
y = df['AQI Value']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and training the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predicting on the test set
y_pred = model.predict(X_test)

# Calculating performance metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Displaying performance metrics
print("Mean absolute Error = ", mae)
print("Mean Square Error = ", mse)
print("Root mean Squared Error", rmse)
print("R-Squared", r2)

# Scatter plot to compare actual vs predicted AQI values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.xlabel('Actual AQI Value')
plt.ylabel('Predicted AQI Value')
plt.title('Actual vs Predicted AQI Values')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal line
plt.show()

# Distribution plot for residuals (errors)
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(residuals, bins=30, kde=True)
plt.title('Distribution of Residuals')
plt.xlabel('Residuals (Actual - Predicted)')
plt.ylabel('Frequency')
plt.show()

# Feature importance plot
feature_importances = model.feature_importances_
features = X.columns
feature_importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Feature Importance in Predicting AQI Value')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()