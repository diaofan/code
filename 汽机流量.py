# coding=gbk
import math
def a(p0,t0,n1,n2,n3,n4,G,p):
    k=p/p0#计算压比
    k1=math.sqrt(1-((k-0.574)/(1-0.574))**2)#计算彭台门系数
    Gmax=G/k1#计算最大流量
    Gmax3=Gmax*(n1+n2+n3)/(n1+n2+n3+n4)#计算III阀点时最大流量
    p23=p*Gmax3/Gmax#计算调节级后压力
    Gmax2=Gmax*(n1+n2)/(n1+n2+n3+n4)#计算II阀点时最大流量
    Gmax1=Gmax*(n1)/(n1+n2+n3+n4)#计算I阀点时最大流量
    print('III阀点时最大流量',Gmax3,'t/h')
    print('II阀点时最大流量',Gmax2,'t/h')
    print('I阀点时最大流量',Gmax1,'t/h')

a(16.67,550,8,6,4,4,1300,10)