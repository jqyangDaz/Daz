library(plotrix)
library(grid)
library(vcd)
library(tseries)                  
#��������İ�
homi<-read.csv('e:/database.csv') 
#¼������
nrow(homi)                       
#�鿴��������
length(homi)                      
#�鿴��������
View(homi)                        
#Ԥ������
attach(homi)                      
bar1<-table(Month)                
#��ȡMonth���ݵĵķ���Ƶ��
barplot(bar1)                     
#��������ͼ
pie1<-table(Year)
pie(pie1,main='��ݺ���ɱ�������ı�ͼ')    
#���Ʊ�ͼ
lals_pct <- paste(names(pie1), " ", round(pie1/sum(pie1), 2)*100, "%", sep="")  
#����ٷֱ�
lals_pct
bar2<-table(Year)
barplot(bar2,main = 'bar of year',col='pink')    
#��������ͼ
pie2<-table(Victim.Sex)                          
#��ȡƵ��
lals_pct1 <- paste(names(pie2), " ", round(pie2/sum(pie2), 2)*100, "%", sep="")     
#����ٷֱ�
pie3D(pie2,labels=lals_pct,main = 'pie of sex',explode=0.1)                         
#����3D��ͼ
pie3<-table(Victim.Race)                                                            
#��ȡƵ��
lals_pct2 <- paste(round(pie3/sum(pie3),2)*100, "%", sep="")                       
#����ٷֱ�
pie(pie3,main ="pie of Vicitim's race",labels = lals_pct2,
    col=c("purple", "violetred1", "green3","cornsilk", "cyan"))                     
#���Ʊ�ͼ
legend(0.8,1.25,names(pie3),fill = c("purple", "violetred1", "green3","cornsilk", "cyan"))                 
#���ӱ�ע
pie4<-table(Perpetrator.Sex)                                                        
#��ȡƵ��
lals_pct3 <- paste(names(pie4), " ", round(pie4/sum(pie4),2)*100, "%", sep="")       
#����ٷֱ�
pie3D(pie4,labels = lals_pct3,explode = 0.1)                                         
#����3D��ͼ
pie5<-table(Perpetrator.Race)                                                        
#��ȡƵ��
lals_pct4 <- paste(names(pie5), " ", round(pie5/sum(pie5),2)*100, "%", sep="")      
#����ٷֱ�
pie(pie5,labels = lals_pct4,main = "pie of Perpetrator's Race")                     
#���Ʊ�ͼ
bar2<-table(Relationship)                                                           
#��ȡƵ��
barplot(bar2,main="Hist of Relationship",col='purple')                              
#��������ͼ
summary(Victim.Age)                                                                 
#�鿴���ݸ�Ҫ
Victimage<-c(Victim.Age)                                                            
#ת��Ϊ����
V<-Victimage[Victimage<998]                                                          
#�ų�����Ϊ998������
summary(V)                                                                           
#�鿴���ݸ�Ҫ
boxplot(V,main = 'box of age',ylab='years')                                         
#��������ͼ
summary(Perpetrator.Age)                                                              
P<-na.omit(Perpetrator.Age)                                                          
#ɾ��ȱʧֵ               
summary(P)
boxplot(P,main = 'box of age',ylab='years')
chisq.test(Victim.Count,Perpetrator.Count)                                          
#��������Ŷȼ���
chisq.test(Year,Weapon)
pie6<-table(Weapon)
lals_pct5 <- paste(names(pie6), " ", round(pie6/sum(pie6),2)*100, "%", sep="")
pie3D(pie6,explode=0.1,labels=lals_pct5)
barplot(pie6,col=c('blue','red','orange','purple','yellow'),main = 'Bar of Weapon')
w1<-subset(homi,Year==1980,select=c(Year,Weapon))                                   
#��ȡ�������������
w2<-subset(homi,Year==1990,select=c(Year,Weapon))
w3<-subset(homi,Year==2000,select=c(Year,Weapon))
w4<-subset(homi,Year==2010,select=c(Year,Weapon))
bar3<-table(w1$Weapon)
bar4<-table(w2$Weapon)
bar5<-table(w3$Weapon)
bar6<-table(w4$Weapon)
par(mfrow=c(2,2))                                                                  
#����ͼʱʹ��2*2��ʽ
barplot(bar3,main = '1980')
barplot(bar4,main = '1990')
barplot(bar5,main = '2000')
barplot(bar6,main = '2010')                                                        
#��������ͼ
fan1<-table(Crime.Solved)
lals_pct6 <- paste(names(pie7), " ", round(pie7/sum(pie7),2)*100, "%", sep="")
fan.plot(pie7,labels = lals_pct6,col=c('pink','blue'),radius=0.8)
r1<-subset(homi,Year==1980,select=c(Year,Crime.Solved))
r2<-subset(homi,Year==1990,select=c(Year,Crime.Solved))
r3<-subset(homi,Year==2000,select=c(Year,Crime.Solved))
r4<-subset(homi,Year==2010,select=c(Year,Crime.Solved))                             
#��ȡ�����Ƿ�᰸������
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
#��ȡ���ݲ�ǿ��ת��Ϊ���ݿ�����
Y<-subset(Y,select = c(counts))
tscounts<- ts(Y,start = c(1980))                                                   
#������ת��Ϊʱ������
plot.ts(tscounts)                                                                  
#����ʱ������ͼ
tscountsdiff<-diff(tscounts,differences=1)                                         
#�����н���һ�ײ��
plot.ts(tscountsdiff)                                                              
#����һ�ײ�ֺ��ͼ
acf(tscountsdiff,lag.max = 20)                              
pacf(tscountsdiff,lag.max = 20)                                                    
#����acf��pacfͼ
counts<-arima(tscountsdiff,order=c(1,0,0))                                         
#����ARģ��
a<-subset(homi,Victim.Age<998,select = c(Year,Victim.Age,Perpetrator.Age))
detach(homi)
attach(a)
par(mfrow=c(1,2))
plot(Victim.Age~Year,main='Year vs Vicitim.Age')
plot(Perpetrator.Age~Year,main='Year vs Perpetrator.Age')
lm.1<-lm(Perpetrator.Count~Perpetrator.Age,data=homi)                              
#�ع�ģ�͵����
summary(lm.1)
#�ع鷽�̽���Ĳ鿴
sex<-subset(homi,Perpetrator.Sex!='Unknown',select=c(Perpetrator.Count,Perpetrator.Sex,Perpetrator.Age))
detach(homi)
attach(sex)
as.factor(Perpetrator.Sex)
#���Ա�ת��Ϊ���ӱ���
lm.2<-lm(Perpetrator.Count~-1+Perpetrator.Sex,data=sex)
#û�нؾ���Ļع����
summary(lm.2)
lm.3<-lm(Perpetrator.Count~-1+Perpetrator.Sex+Perpetrator.Age,data=sex)
#û�нؾ���Ķ�Ԫ���Իع�
summary(lm.3)