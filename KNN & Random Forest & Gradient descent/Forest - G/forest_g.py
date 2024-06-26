# -*- coding: utf-8 -*-
"""Forest - G.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M3hQCLAr59VKWWqhMTGHk7ZCX6S1NQ5P
"""

import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import learning_curve

y = np.load('/content/drive/MyDrive/hw1/y.npy')
x = np.load('/content/drive/MyDrive/hw1/x.npy')
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.1)     #split data_set for training and test
R_Forest = RandomForestClassifier()         #create instance of random-forest
R_Forest.fit(x_train, y_train)              # train the random-forest
accuracy = R_Forest.score(x_test, y_test)   #count accuracy
print(accuracy)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.1)       #split data_set for training and test
Gradient = GradientBoostingClassifier()                               #create instance of gradientboosting
Gradient.fit(x_train, y_train)                                        #train the random-forest
accuracy = Gradient.score(x_test, y_test)                             #count accuracy
print(accuracy)

train_sizes, train_accuracy, validation_accuracy = learning_curve(       #return The sizes of training sets uses in cross-validation  and  The training scores at each training size  and The cross-validated validation scores at each training size
estimator = R_Forest,
X = x,
y = y,
train_sizes = [0.25, 0.5, 0.75, 1],   #training percent
cv = 8,                                 #split training data to 8 parts and train 8 times (validation)
scoring = 'accuracy')

#return a matrix of train_seize and cv accuracy

train_mean = np.mean(train_accuracy, axis=1)  #count the mean of each row(each training size   0.25 0.5 ...)
train_enheraf = np.std(train_accuracy, axis=1)    #count the standard_deviation of each row(each training size 0.25 0.5 ...)               #act on training set
test_mean = np.mean(validation_accuracy, axis=1) #count the mean of each row(each training size   0.25 0.5 ...)
test_enheraf = np.std(validation_accuracy, axis=1)   #count the standard_deviation of each row(each training size 0.25 0.5 ...)            #act on validation set


plt.title("Learning Curve")
plt.xlabel("Training Examples")
plt.ylabel("Accuracy")

up = train_mean + train_enheraf
down = train_mean - train_enheraf

plt.plot(train_sizes, train_mean, marker='o', color="navy", label="Training score")

plt.fill_between(train_sizes, down , up , alpha=0.1, color="deeppink")  #enheraf meyar atraf khat



up = test_mean + test_enheraf
down = test_mean - test_enheraf

plt.plot(train_sizes, test_mean, marker='o', color="lightseagreen", label="validation score")

plt.fill_between(train_sizes,down,up, alpha=0.1, color="lime")     #enheraf meyar atraf khat


plt.legend()
plt.xlim(0, 4100)
plt.show()



train_sizes, train_accuracy, validation_accuracy = learning_curve(       #return The sizes of training sets uses in cross-validation  and  The training scores at each training size  and The cross-validated validation scores at each training size
estimator = Gradient,
X = x,
y = y,
train_sizes = [0.25, 0.5, 0.75, 1],   #training percent
cv = 8,                                 #split training data to 8 parts and train 8 times (validation)
scoring = 'accuracy')

#return a matrix of train_seize and cv accuracy

train_mean = np.mean(train_accuracy, axis=1)  #count the mean of each row(each training size   0.25 0.5 ...)
train_enheraf = np.std(train_accuracy, axis=1)    #count the standard_deviation of each row(each training size 0.25 0.5 ...)               #act on training set
test_mean = np.mean(validation_accuracy, axis=1) #count the mean of each row(each training size   0.25 0.5 ...)
test_enheraf = np.std(validation_accuracy, axis=1)   #count the standard_deviation of each row(each training size 0.25 0.5 ...)            #act on validation set


plt.title("Learning Curve")
plt.xlabel("Training Examples")
plt.ylabel("Accuracy")

up = train_mean + train_enheraf
down = train_mean - train_enheraf

plt.plot(train_sizes, train_mean, marker='o', color="navy", label="Training score")

plt.fill_between(train_sizes, down , up , alpha=0.1, color="deeppink")  #enheraf meyar atraf khat



up = test_mean + test_enheraf
down = test_mean - test_enheraf

plt.plot(train_sizes, test_mean, marker='o', color="lightseagreen", label="validation score")

plt.fill_between(train_sizes,down,up, alpha=0.1, color="lime")     #enheraf meyar atraf khat


plt.legend()
plt.xlim(0, 4100)
plt.show()