import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
from statsmodels.tsa.stattools import adfuller,acf,pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import matplotlib.pyplot as plt
from sklearn import metrics as me

data1=pd.read_csv('e:/work/milkproduction.csv',header=0,index_col=0)
data1=pd.Series(data1['production'])

data1_diff=data1.diff(1).dropna()
x=pd.concat([data1_diff, data1],axis=1)
print(x)

print(adfuller(data1_diff,autolag='AIC'))


model=ARIMA(data1_diff,order=(1,0,2)).fit(disp=-1)
print(sum((data1_diff-model.fittedvalues)**2))
exit()
'''
model.plot_predict()
model.forecast()
plot_acf(data1)
plot_pacf(data1)
sm.qqplot(model.resid,line='s')
plt.show()
'''

model_prediction_diff=pd.Series([data1[0],data1[1]-data1[0]],index=[data1.index[0],data1.index[1]])\
    .append(model.fittedvalues)
model_prediction=pd.Series.cumsum(model_prediction_diff)
model_prediction.plot()
data1.plot()
plt.show()


