# -*- coding: utf-8 -*-
"""Vehicle Fuel Consumption and Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZkvL5V2EaT1j8R11XGERz4uvB701fmm_

Installing and Importing required libraries
and Load the Dataset
"""

pip install dataprep

import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import tensorflow as tf
from dataprep.eda import plot, plot_correlation
pd.set_option('display.max_columns', 50)
df=pd.read_csv('Consumption Ratings 2023 (1).csv',encoding=('ISO-8859-1'),dtype={'Vehicle Class':'category', 'Transmission':'category', 'Fuel Type':'category'})
df

"""Exploratory Data Analysis(EDA)"""

df.head()

df.tail()

df.isna().sum()

df.dropna(inplace=True)

df.isna().sum()

df.info()

df.duplicated().sum()

df.describe()

corr=df.corr()
corr

sns.heatmap(corr,annot=True)

"""Visualizing important insights and Stats from the Dataset"""

plot(df)

plot(df, 'Make', 'Model')

plot(df, 'Model', 'Year')

plot(df, 'Make', 'Vehicle Class')

plot(df, 'Make', 'Engine Size (L)')

plot(df, 'Make', 'Cylinders')

plot(df, 'Make', 'Fuel Type')

plot(df, 'Make', 'Transmission')

plot(df, 'Make', 'Smog Rating')

"""Fuel Type Analysis"""

data = pd.melt(df, id_vars='Fuel Type', value_vars=['Fuel Consumption (L/100Km)', 'Hwy (L/100 km)', 'Comb (L/100 km)', 'Comb (mpg)', 'CO2 Emissions (g/km)'])
px.box(data, x='Fuel Type', y='value', color='variable', title='Fuel Type Analysis').show()

"""Transmission Type Analysis"""

data = pd.melt(df, id_vars='Transmission', value_vars=['Fuel Consumption (L/100Km)', 'Hwy (L/100 km)', 'Comb (L/100 km)', 'Comb (mpg)', 'CO2 Emissions (g/km)'])
px.box(data, x='Transmission', y='value', color='variable', title='Transmission Type Analysis').show()

plot_correlation(df)

"""Removing Irrevelant Features"""

df=df.drop(['Transmission','Make','Year','Vehicle Class','Model'],axis=1)

"""Label Encoding"""

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

"""Applying Label encoding to each categorical column"""

categorical_columns = ['Fuel Type']
for column in categorical_columns:
    df[column] = label_encoder.fit_transform(df[column])

df.head()

"""Define features and the target variable"""

X = df.drop(['CO2 Emissions (g/km)'],axis=1)
y = df['CO2 Emissions (g/km)']

"""Importing Required Linear Regression libraries"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

"""Data Splitting"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""Model Building and selection"""

model = LinearRegression()

"""Model Training"""

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

"""Evaluation"""

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

"""Scatter Plot with Regression Line"""

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='b', alpha=0.8, edgecolors='k', s=100)
sns.regplot(x=y_test, y=y_pred, scatter=False, color='y', line_kws={"color": "y", "lw": 2})
plt.xlabel("Actual Values", fontsize=14)
plt.ylabel("Predicted Values", fontsize=14)
plt.title("Model Performance - Actual vs. Predicted Values", fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()