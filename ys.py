
name=input('Please enter your name: ')
print('hello world',name)


print(r'''hello,\n
world''')
s1=72
s2=85
print(s2/s1-1)
print(r'''Xiao'M's grades grows %f %%''' %((s2/s1-1)*100))
print(r'''hsdaas\[d/cv,dfdfvcvello worl'
      d''')
s1=int(input('Please enter your first grade\n:'))
s2=int(input(r'''Please enter your second grade
:'''))
print(r'''The growth rate is%f %%'''%((s2/s1-1)*100))


classmates=['Y','J','Q']
len(classmates)
classmates.append('W')
classmates.insert(1, 'Jack')
classmates.pop(2)    #删除
classmates[3]='Bob'
s = ['python', 'java', ['asp', 'php'], 'scheme']
t1=('bu','neng','gai')
t2=(1,)
t3=('z','c',['n','b'])
t3[2][1]='gaibian'
#改变的不是tuple
age=int(input(r'''Please enter your age
:'''))
if age>=18:
     print('your age is:',age)
else:
     print('you are teenagers')



 age = int(input(r'''Please enter your age
     :'''))
     if age >= 18:
         print('your age is:', age)
     elif age > 10:
         print('you are teenagers')
     elif age <= 10:
         print('kid')

height=float(input(r'''Please enter your height
单位：米'''))
weight=float(input(r'''Please enter your weight
单位：千克'''))
bmi=weight/height**2
if bmi<18.5:
     print('太轻')
elif bmi<=25:
     print('normal')
elif bmi<=28:
    print('too heavy')
elif bmi<=32:
     print('肥胖')
else:
     print('严重肥胖')

for i in range(101):
	sum=sum+i

L=['Bart','Lisa','Adam']
for name in L:
     print(r'''hello
,''',name)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
d['Tom']=100
d.pop('Tom ')

s=set[(1,2,3,'ff')]
s.add(4)
s.remove('ff')            #就是集合

a=[3,2,4,5]
a.sort()
b='dfg'
b.replace('d','D')
b=b.replace('d','D')


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    x = ((-b) + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    y = ((-b) - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x, y
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

import math


def power(x, n=2):             #默认n=2
    s = 1
    f = 1
    if n > 0:
        while n > 0:
            s = s * x
            n = n - 1
        return s
    elif n < 0:
        while n < 0:
            f = f * x
            n = n + 1
        return 1 / f
    else:
        return 1

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):   #把numbers变为可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def person(name,age,**kw):  #**为可选参数
    print('name:',name,'age:',age,'other:',kw)

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

def person(name, age, *, city, job):    #必须存在*后面的参数的key
    print(name, age, city, job)

def person(name, age, *, city='Beijing', job):  #也可存在缺省值
    print(name, age, city, job)

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)         #递归函数

def factor(n):
    s=1
    while n>=1:
        s=s*n
        n=n-1
    return s                   #上一个程序更简洁

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        hanoi(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上

def trim(s):
    if s[0]==' ':
        s=s[1:]
        return trim(s)
    elif s[-1]==' ':
        s=s[:-1]
        return trim(s)
    else:
        return s

def findMinAndMax(L):
    x=L[0]
    y=L[0]
    for i in  L:
        if x<i:
            x=i
    for j in L:
        if y>j:
            y=j
    return x,y

z=[x*x for x in range(1,10)]




import numpy as np
data1=[6,7.5,8,0,1]
arr1=np.array(data1)
data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
arr2.ndim
arr2.shape
np.zeros(10)
np.eye(n)
np.zeros((1,2,3))

arr=np.arange(10)
arr_slice=arr[5:8]
arr_slice[1]=12231     #arr一起改变
arr_slice=arr[5:8].copy()   #不会改变
data=np.random.randn(7,4)   #7行4列矩阵正态分布
name=np.array([True,False,True,True,False,False,False])
data[name,2]
data[data<0]=0
arr=np.zeros([8,8])
for i in range(8):
    arr[i]=i
arr[[4,3,0,6]]    #花式索引
arr[[np.ix_([1,5,7,2],[0,3,1,2])]] #重排矩阵
arr.T
np.dot(arr.T,arr)
np.exp(arr)
np.sqrt(arr)
#numpy中有很多数学函数
np.meshgrid(x,y)  #行y，列x
xarr=np.array([1.1,1.2,1.3,1.4])
yarr=np.array([2.1,2.2,2.3,2.4])
cond=np.array([True,False,True,False])
data=np.where(cond,xarr,yarr)
arr.any()
arr.all()
a=[(xarr if xarr>yarr else yarr) for xarr,yarr in zip(xarr,yarr)]   #三元运算符
arr.sum(0)
arr.sum(1)
arr.mean(0)
arr.cumsum()
arr.cumprod()
(arr>0).sum()
arr.sort()
np.unique(arr)
np.intersect1d(arr,arr2)#交
np.union1d(arr,arr2)#并
np.in1d(arr,arr2)#arr中的元素是否在arr2中，返回布尔值
np.setdiff1d(arr,arr2)#arr-arr2
np.setxord1d(arr,arr2)#对称差,不同时在两个中
np.load()
np.save()
np.savez()
np.dot()
from numpy.linalg import inv,qr


steps=1000
draw=np.random.randint(0,2,size=steps)
step=np.where(draw>0,1,-1) #draw>0 取 1 反之取-1
walk=step.cumsum()





###Pandas
import pandas as pd
arr=pd.Series([13,-2,34,1])
arr.values
arr.index
arr=pd.Series([2,3,1,2],index=['a','b','c','d'])

sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj4=pd.Series(sdata)               #字典直接转化成Series
obj3=pd.Series(sdata,index=['Ohio','Texas','Oregon','Calfornia'])    #去除不在index中的
pd.isnull(obj3)
obj3+obj4
obj4.name='Population'
obj4.index.name='state'


data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=pd.DataFrame(data)
frame=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['a','b','c','d','e'])
frame['debt']=[16,12,13,12,4]
frame['debt']=np.arange(5)
val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame['debt']=val
frame['eastern']=frame['state']=='Ohio'
del frame['eastern']
frame.T
index=pd.Index(np.range(3))
obj2=obj.reindex(['a','b','c','d','e'])#重排index，没有的用缺失值填补
obj2=obj.reindex(['a','b','c','d','e']，)#重排index，没有的用0填补
frame=pd.DataFrame(np.arange(12).reshape(4,3),index=['Ohio','Utah','Texas','Oregon'],columns=list('bde'))
S=pd.Series(frame.ix[0])
series=frame.ix[0]
####add,sub,div,mul 加减除乘
def f(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])  #返回最大最小值
frame.applymap(f)
frame.apply(f)
series.map(f)#元素级
frame.sort_index(axis=1,ascending=False) #排序，默认参数为0，True
obj.sort_values()# 对series进行排序，nan默认排最后
frame.sort_index(by='b')
frame.rank(method='first,max,min')
obj=pd.Series(np.arange(5),index=['a','a','b','c','d'])  #可以一样的index
obj.index.is_unique
df=pd.DataFrame(np.random.normal(5,4,size=(4,3)),index=['a','a','b','c'],columns=['one','two','three'])
frame.rename(index={'a':'f'})#数据框改名
frame.mean(skipna=False)
frame=pd.DataFrame((np.arange(12).reshape(4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
###层次化索引
frame.index.names=['key1','key2']
frame.columns.names=['State','color']
frame.swaplevel('key1','key2')#交换级别
frame.swaplevel(0,1).sortlevel(1)
pd.Panel#面板数据
df.to_csv('bass.csv ')

###matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(2,2,1)
plt.plot(np.random.randn(50),'k--')
ax.scatter(np.random.randn(100),np.range.randint(0,2,size=100))
