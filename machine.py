import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn import linear_model as lm
from sklearn import  datasets
from sklearn import cross_validation as cv
from sklearn import metrics as me
from sklearn.preprocessing import StandardScaler
from IPython.display import Image
import pydotplus


'''
data=pd.read_excel("e:/work/CCPP/Folds5x2_pp.xlsx",sheet_name=0,header=0)
X=data[['AT','V','AP','RH']]
y=data[['PE']]
X_train,X_test,y_train,y_test=cv.train_test_split(X,y,random_state=3)
'''
'''
逻辑回归
y=np.random.randint(0,2,9568)
model=lm.LogisticRegression()
model.fit(X_train,y_train)
print(model.coef_)
print(model.intercept_)
y_pred=model.predict(X_test)
length=len(y_pred)
'''
'''
线性回归
model=lm.LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
length=len(y_pred)
print(model.score(X_test,y_test))
print(me.mean_squared_error(y_test,y_pred))
'''
'''
#决策树的实现
plot_step = 0.02
iris=datasets.load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=cv.train_test_split(x,y,random_state=3)
clf=tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(x,y)
y_pred=clf.predict(x_test)
x_min, x_max = x[:, 0].min(), x[:, 0].max()

y_min, y_max = x[:, 1].min(), x[:, 1].max()

xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),

                     np.arange(y_min, y_max, plot_step))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

Z = Z.reshape(xx.shape)

cs = plt.contourf(xx, yy, Z, cmap=plt.cm.BrBG)
'''
'''
#神经网络的实现

'''

'''
plt.plot(np.arange(length),y_pred,'k--',label='predict')
plt.plot(np.arange(length),y_test,'r--',label='test')
plt.xlim((0,50))
plt.legend(loc='upper right')
plt.xlabel('numbers')
plt.show()



print(me.mean_squared_error(y_pred,y_test))
print(model.score(X_test,y_test))
exit()

#plt.scatter(data['AT'],data['V'])
#x=np.random.normal(5,10,500)
#y=np.random.chisquare(5,500)
#model.fit(x,y)
plt.plot(data['AT'],data['V'],"k--")
plt.show()
'''
np.random.seed(3)
X,y=datasets.make_moons(200,noise=0.2)
X_train,X_test,y_train,y_test=cv.train_test_split(X,y)
clf=lm.LogisticRegression()
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
length=len(y_pred)


