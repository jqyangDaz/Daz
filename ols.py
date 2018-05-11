import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import random
import numpy as np
list=['a','a','b','c','c','c','c']
time=[]
for i in range(13):
    list.append('d')
for z in range(100):
    a=3
    type = []
    for i in range(100):
        if random.choice(list)=='a':
            type.append('a')
        elif random.choice(list)=='b':
            type.append('b')
        elif random.choice(list)=='c':
            type.append('c')
        else:
            type.append('d')
    while True:
        if ('a' in type[0:a])&('b' in type[0:a])&('c' in type[0:a]):
            break
        else:
            a=a+1
            continue
    time.append(a)
print(np.mean(time))
exit()









df=pd.read_csv('e:/study/province.csv')
df=df.dropna()
res=sm.ols(formula='Fertility~PPgdp+Purban',data=df).fit()
res.summary()

import numpy as np
import pandas as pd
import statsmodels.formula.api as sm
import statsmodels.api as smf
df=pd.read_csv('e:/study/province.csv')
df=df.dropna()
y=np.array(df['Fertility'])
x1=np.array(df['PPgdp'])
x2=np.array(df['Purban'])
y=np.log(y)
x1=np.log(x1)
x2=np.log(x2)
X=np.column_stack((x1,x2))
X=smf.add_constant(X)
res=smf.OLS(y,X).fit()
res.summary()