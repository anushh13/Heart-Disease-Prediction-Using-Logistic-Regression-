from warnings import filterwarnings
filterwarnings('ignore')
import os
os.chdir('C:\dataset')
import os
print(os.getcwd())  # This prints the current working directory
print(os.listdir())  # This lists all files in the current directory
import pandas as pd

# Replace 'path/to/your/framingham.csv' with the actual path to your file
file_path = 'path/to/your/framingham.csv'

# Load the CSV file
df = pd.read_csv('framingham.csv')
df.head()

import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
import statsmodels.api as sm
from sklearn import preprocessing
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sn

# dataset
disease_df = pd.read_csv("framingham.csv")
disease_df.drop(['education'], inplace=True, axis=1)
disease_df.rename(columns={'male': 'Sex_male'}, inplace=True)

# removing NaN / NULL values
disease_df.dropna(axis=0, inplace=True)
print(disease_df.head(), disease_df.shape)
print(disease_df.TenYearCHD.value_counts())
# counting no. of patients affected with CHD
plt.figure(figsize=(7, 5))
sn.countplot(x='TenYearCHD', data=disease_df,
             palette="BuGn_r")
plt.show()
laste = disease_df['TenYearCHD'].plot()
plt.show(laste)
laste = disease_df['TenYearCHD'].plot()
plt.show(laste)
X = np.asarray(disease_df[['age', 'Sex_male', 'cigsPerDay',
                           'totChol', 'sysBP', 'glucose']])
y = np.asarray(disease_df['TenYearCHD'])
 
# normalization of the dataset
X = preprocessing.StandardScaler().fit(X).transform(X)
 
# Train-and-Test -Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.3, random_state = 4)
 
 
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)
from sklearn.linear_model import LogisticRegression
 
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
 
# Evaluation and accuracy
from sklearn.metrics import jaccard_score
 
print('')
print('Accuracy of the model in jaccard similarity score is = ',
     jaccard_score (y_test, y_pred))
      # This code is contributed by @amartajisce
from sklearn.ensemble import RandomForestClassifier
 
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
 
score = rf.score(X_test,y_test)*100
print('Accuracy of the model is = ', score)
# Confusion matrix
from sklearn.metrics import confusion_matrix, classification_report
 
cm = confusion_matrix(y_test, y_pred)
conf_matrix = pd.DataFrame(data = cm,
                           columns = ['Predicted:0', 'Predicted:1'],
                           index =['Actual:0', 'Actual:1'])
 
plt.figure(figsize = (8, 5))
sn.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = "Greens")
 
plt.show()
 
print('The details for confusion matrix is =')
print (classification_report(y_test, y_pred))
 
# This code is contributed by parna_28