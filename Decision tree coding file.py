# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 05:25:07 2020

@author: Precious
"""



#Importing Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#Importing Dataset
Data = pd.read_csv('Iris.csv')

#Summary of the Dataset
Data.describe()

#Checking for Potential Null values
Data.isnull().any()

#To chck the relationship between columns
sns.pairplot(Data, hue = 'Species')

#Splitting the datasets
X =Data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
Y = Data['Species'].values
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.7, random_state = 2)

#Implementing Decision tree classifier 
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train, Y_train)
Prediction = dtc.predict(X_test)

#Evaluating the model to check accuracy
from sklearn.metrics import accuracy_score
score = accuracy_score(Y_test, Prediction)

score