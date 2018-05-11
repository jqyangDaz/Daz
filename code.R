library(plotrix)
library(grid)
library(vcd)
library(tseries)                  
#导入所需的包
homi<-read.csv('e:/database.csv') 
#录入数据
nrow(homi)                       
#查看数据行数
length(homi)                      
#查看数据列数
View(homi)                        
#预览数据
attach(homi)                      
bar1<-table(Month)                
#获取Month数据的的分类频数
barplot(bar1)                     
#绘制条形图
pie1<-table(Year)
pie(pie1,main='年份和凶杀案数量的饼图')    
#绘制饼图
lals_pct <- paste(names(pie1), " ", round(pie1/sum(pie1), 2)*100, "%", sep="")  
#计算百分比
lals_pct
bar2<-table(Year)
barplot(bar2,main = 'bar of year',col='pink')    
#绘制条形图
pie2<-table(Victim.Sex)                          
#获取频数
lals_pct1 <- paste(names(pie2), " ", round(pie2/sum(pie2), 2)*100, "%", sep="")     
#计算百分比
pie3D(pie2,labels=lals_pct,main = 'pie of sex',explode=0.1)                         
#绘制3D饼图
pie3<-table(Victim.Race)                                                            
#获取频数
lals_pct2 <- paste(round(pie3/sum(pie3),2)*100, "%", sep="")                       
#计算百分比
pie(pie3,main ="pie of Vicitim's race",labels = lals_pct2,
    col=c("purple", "violetred1", "green3","cornsilk", "cyan"))                     
#绘制饼图
legend(0.8,1.25,names(pie3),fill = c("purple", "violetred1", "green3","cornsilk", "cyan"))                 
#添加标注
pie4<-table(Perpetrator.Sex)                                                        
#获取频数
lals_pct3 <- paste(names(pie4), " ", round(pie4/sum(pie4),2)*100, "%", sep="")       
#计算百分比
pie3D(pie4,labels = lals_pct3,explode = 0.1)                                         
#绘制3D饼图
pie5<-table(Perpetrator.Race)                                                        
#获取频数
lals_pct4 <- paste(names(pie5), " ", round(pie5/sum(pie5),2)*100, "%", sep="")      
#计算百分比
pie(pie5,labels = lals_pct4,main = "pie of Perpetrator's Race")                     
#绘制饼图
bar2<-table(Relationship)                                                           
#获取频数
barplot(bar2,main="Hist of Relationship",col='purple')                              
#绘制条形图
summary(Victim.Age)                                                                 
#查看数据概要
Victimage<-c(Victim.Age)                                                            
#转换为向量
V<-Victimage[Victimage<998]                                                          
#排除年龄为998的数据
summary(V)                                                                           
#查看数据概要
boxplot(V,main = 'box of age',ylab='years')                                         
#绘制箱线图
summary(Perpetrator.Age)                                                              
P<-na.omit(Perpetrator.Age)                                                          
#删除缺失值               
summary(P)
boxplot(P,main = 'box of age',ylab='years')
chisq.test(Victim.Count,Perpetrator.Count)                                          
#卡放拟合优度检验
chisq.test(Year,Weapon)
pie6<-table(Weapon)
lals_pct5 <- paste(names(pie6), " ", round(pie6/sum(pie6),2)*100, "%", sep="")
pie3D(pie6,explode=0.1,labels=lals_pct5)
barplot(pie6,col=c('blue','red','orange','purple','yellow'),main = 'Bar of Weapon')
w1<-subset(homi,Year==1980,select=c(Year,Weapon))                                   
#提取各年的武器数据
w2<-subset(homi,Year==1990,select=c(Year,Weapon))
w3<-subset(homi,Year==2000,select=c(Year,Weapon))
w4<-subset(homi,Year==2010,select=c(Year,Weapon))
bar3<-table(w1$Weapon)
bar4<-table(w2$Weapon)
bar5<-table(w3$Weapon)
bar6<-table(w4$Weapon)
par(mfrow=c(2,2))                                                                  
#绘制图时使用2*2格式
barplot(bar3,main = '1980')
barplot(bar4,main = '1990')
barplot(bar5,main = '2000')
barplot(bar6,main = '2010')                                                        
#绘制条形图
fan1<-table(Crime.Solved)
lals_pct6 <- paste(names(pie7), " ", round(pie7/sum(pie7),2)*100, "%", sep="")
fan.plot(pie7,labels = lals_pct6,col=c('pink','blue'),radius=0.8)
r1<-subset(homi,Year==1980,select=c(Year,Crime.Solved))
r2<-subset(homi,Year==1990,select=c(Year,Crime.Solved))
r3<-subset(homi,Year==2000,select=c(Year,Crime.Solved))
r4<-subset(homi,Year==2010,select=c(Year,Crime.Solved))                             
#提取案件是否结案的数据
fan2<-table(r1$Crime.Solved)
fan3<-table(r2$Crime.Solved)
fan4<-table(r3$Crime.Solved)
fan5<-table(r4$Crime.Solved)
par(mfrow=c(2,2))
lals_pct7 <- paste(names(fan2), " ", round(fan2/sum(fan2),2)*100, "%", sep="")
lals_pct8 <- paste(names(fan3), " ", round(fan3/sum(fan3),2)*100, "%", sep="")
lals_pct9 <- paste(names(fan4), " ", round(fan4/sum(fan4),2)*100, "%", sep="")
lals_pct10 <- paste(names(fan5), " ", round(fan5/sum(fan5),2)*100, "%", sep="")
pie(fan2,col=c('pink','blue'),labels=lals_pct7,radius=0.8,main='1980')
pie(fan3,col=c('pink','blue'),labels=lals_pct8,radius=0.8,main='1990')
pie(fan4,col=c('pink','blue'),labels=lals_pct9,radius=0.8,main='2000')
pie(fan5,col=c('pink','blue'),labels=lals_pct10,radius=0.8,main = '2010')
Y<-as.data.frame(table(Year))                                                     
#提取数据并强制转化为数据框类型
Y<-subset(Y,select = c(counts))
tscounts<- ts(Y,start = c(1980))                                                   
#将数据转化为时间序列
plot.ts(tscounts)                                                                  
#绘制时间序列图
tscountsdiff<-diff(tscounts,differences=1)                                         
#将序列进行一阶差分
plot.ts(tscountsdiff)                                                              
#绘制一阶差分后的图
acf(tscountsdiff,lag.max = 20)                              
pacf(tscountsdiff,lag.max = 20)                                                    
#绘制acf和pacf图
counts<-arima(tscountsdiff,order=c(1,0,0))                                         
#构建AR模型
a<-subset(homi,Victim.Age<998,select = c(Year,Victim.Age,Perpetrator.Age))
detach(homi)
attach(a)
par(mfrow=c(1,2))
plot(Victim.Age~Year,main='Year vs Vicitim.Age')
plot(Perpetrator.Age~Year,main='Year vs Perpetrator.Age')
lm.1<-lm(Perpetrator.Count~Perpetrator.Age,data=homi)                              
#回归模型的拟合
summary(lm.1)
#回归方程结果的查看
sex<-subset(homi,Perpetrator.Sex!='Unknown',select=c(Perpetrator.Count,Perpetrator.Sex,Perpetrator.Age))
detach(homi)
attach(sex)
as.factor(Perpetrator.Sex)
#将性别转化为因子变量
lm.2<-lm(Perpetrator.Count~-1+Perpetrator.Sex,data=sex)
#没有截距项的回归拟合
summary(lm.2)
lm.3<-lm(Perpetrator.Count~-1+Perpetrator.Sex+Perpetrator.Age,data=sex)
#没有截距项的多元线性回归
summary(lm.3)
