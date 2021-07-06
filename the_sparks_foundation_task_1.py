# -*- coding: utf-8 -*-
"""The Sparks Foundation Task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16nLuQdTRBPURRZ5lnInkSd50s6O31Uvb

###**The Sparks Foundaton - GRIP July 2021**

###**Prashant Jain**

#### **Task-1 (Level -Beginner)**

**Problem Statement : The percentage of an student based on the no. of study hours.**

Simple Linear Regression in this regression, we will predict the percentage of marks of students based on the numbers of study hours.

###**Importing Essential Libraries**
"""

# Commented out IPython magic to ensure Python compatibility.
# Importing all the essential libraries
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

"""###**Loading the Data**"""

# Reading data
url = "http://bit.ly/w-data"
dataset = pd.read_csv(url)
print("Data imported successfully")

#displaying top Ten rows in the dataset
dataset.head(10)

#size of the dataset
dataset.shape

#columns for the dataset
dataset.columns

# displaying null values and unique values in the dataset
temp=pd.DataFrame({'null_values': dataset.isnull().sum(),'number_of_unique values' : dataset.nunique()})

temp

#datatype of columns
dataset.dtypes

dataset.describe()

# Plotting the distribution of scores
plt.scatter(x=dataset['Hours'],y=dataset['Scores'],color = 'red')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()

"""**From the graph above, we can clearly see that there is a positive linear relation between the number of hours studied and percentage of score.**

###**Preparing the data**
"""

#Seggregating the Dependent or Independent variable

features=dataset.iloc[:, :-1].values
labels=dataset.iloc[:,-1].values

features

labels

#Spliting the dataset into training and testing Set
features_train, features_test, labels_train, labels_test=train_test_split(features,labels,
                                                                          test_size=0.2,random_state=0)

features_train

labels_train

features_test

labels_test

"""###**Training the Model**"""

regressor=LinearRegression()
regressor.fit(features_train,labels_train)

print("Training complete.")

print("Regressor slope:  %2.f  "%( regressor.coef_))
print("Regressor intercept:%2.f  "% regressor.intercept_)

# Visualising the Training set results
plt.scatter(features_train, labels_train, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()

"""###**Making Predictions**"""

# Testing data - In Hours
print(features_test) 

# Predicting the scores
y_pred = regressor.predict(features_test)

y_pred

# Comparing Actual vs Predicted
df = pd.DataFrame({'Actual': labels_test, 'Predicted': y_pred})  
df

print("Training Score: ",regressor.score(features_train,labels_train))
print("Testing Score:",regressor.score(features_test,labels_test))

#plotting the actual and predictedvalue in the bar chart
df.plot(kind='bar',figsize=(7,5))
plt.show()

print('Mean Absolute Error:', 
      mean_absolute_error(labels_test,y_pred)) 

print('Mean Squared Error: ',mean_squared_error(labels_test,y_pred))

#@title Predict the percentage of an student based on the no. of study hours.

Hours_Studied =   9.25#@param {type: "number", min: 1, max: 24} 
own_pred = regressor.predict([[Hours_Studied]])
print("No of Hours_Studied = {}".format(Hours_Studied))
print("Predicted Score = {}".format(own_pred[0]))

