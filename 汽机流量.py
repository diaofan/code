# coding=gbk
import math
def a(p0,t0,n1,n2,n3,n4,G,p):
    k=p/p0#����ѹ��
    k1=math.sqrt(1-((k-0.574)/(1-0.574))**2)#������̨��ϵ��
    Gmax=G/k1#�����������
    Gmax3=Gmax*(n1+n2+n3)/(n1+n2+n3+n4)#����III����ʱ�������
    p23=p*Gmax3/Gmax#������ڼ���ѹ��
    Gmax2=Gmax*(n1+n2)/(n1+n2+n3+n4)#����II����ʱ�������
    Gmax1=Gmax*(n1)/(n1+n2+n3+n4)#����I����ʱ�������
    print('III����ʱ�������',Gmax3,'t/h')
    print('II����ʱ�������',Gmax2,'t/h')
    print('I����ʱ�������',Gmax1,'t/h')

a(16.67,550,8,6,4,4,1300,10)