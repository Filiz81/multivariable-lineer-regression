# -*- coding: utf-8 -*-
"""multyvariablelinearRegression

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L79ruiLwzXRDm2GD2nhTld0Aa_9f9v-9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

x=diabetes.data
y=diabetes.target

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
lin_reg=LinearRegression()
lin_reg.fit(x_train,y_train)
y_pred=lin_reg.predict(x_test)

rmse=np.sqrt(mean_squared_error(y_test,y_pred))
print(rmse)