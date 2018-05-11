#coding=utf-8
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
import itertools

data=pd.read_excel('e:/work/datanew.xlsx',sheet_name=1,header=0,index_col=0)
data1=pd.Series(data['net_cnbd'])
'''
data1=data1.dropna() #去除na值
data1.plot(color='black')
plt.title('old series')
plt.show()    #原始序列画图
print(adfuller(data1,autolag='AIC'))   #序列不平稳
'''
data1_diff=data1.diff(1).dropna()  #一阶差分
'''
data1_diff.plot()
plt.title('new series')
plt.show()  #序列画图
print(adfuller(data1_diff,autolag='AIC'))  #序列平稳,p值通过检验


plot_acf(data1_diff,lags='20')
plot_pacf(data1_diff,lags='20')
plt.show()#定阶
p=d=q=range(0,4)
pdq=list(itertools.product(p,d,q))
for param in pdq:
    try:
        model=ARIMA(data1_diff,order=param).fit(disp=-1)
        print('ARIMA{} AIC:{} BIC:{}'.format(param,model.aic,model.bic))
    except:
        continue



'''
####模型拟合####
model=ARIMA(data1_diff,order=(3,0,3)).fit(disp=-1)
print(model.summary())

model.plot_predict()
model.forecast()
sm.qqplot(model.resid,line='s')
plt.show()

####差分还原画图####
model_prediction_diff=pd.Series([data1[0],data1[1]-data1[0]],index=[data1.index[0],data1.index[1]])\
    .append(model.fittedvalues)
model_prediction=pd.Series.cumsum(model_prediction_diff)
model_prediction.plot(label='forcest')
data1.plot()
plt.legend(loc='upper right')
plt.show()
