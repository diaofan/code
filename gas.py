# coding=gbk
from prettytable import PrettyTable  

def gas_characteristics(Cdaf,Hdaf,Odaf,Ndaf,Sdaf,Aar,Mar,Vdaf,Alpha_fa,Alpha_av):#������������
    Car=(100-Mar-Aar)/100*Cdaf#���Ƚ������޻һ��µ�Ԫ�سɷ�ת��Ϊ�յ���
    Har=(100-Mar-Aar)/100*Hdaf
    Oar=(100-Mar-Aar)/100*Odaf
    Nar=(100-Mar-Aar)/100*Ndaf
    Sar=(100-Mar-Aar)/100*Sdaf
    V0=1/0.21*(1.866*Car/100+5.56*Har/100+0.7*Sar/100-0.7*Oar/100)#���ۿ�����
    VRO2=1.866*(Car+0.375*Sar)/100#��ԭ���ݻ�
    V0H2O=0.111*Har+0.0124*Mar+0.0161*V0#����ˮ�����ݻ�
    V0N2=0.79*V0+22.41/28*Nar/100#���۵����ݻ�
    V0g=VRO2+V0N2+V0H2O#���������ݻ�
    DeltaV=V0*(Alpha_av-1)#��ʣ������
    VH2O=V0H2O+0.0161*DeltaV#ˮ�����ݻ�
    Vg=VRO2+V0N2+DeltaV+VH2O#�������ݻ�
    rRO2=VRO2/Vg#RO2����ռ�����ݻ��ݶ�
    rH2O=VH2O/Vg#ˮ����ռ�����ݻ��ݶ�
    r=rRO2+rH2O#��Ԫ�������ˮ����ռ�����ݻ��ݶ�֮��
    Gg=1-Aar/100+1.306*Alpha_av*V0#��������
    mu=Aar*Alpha_fa/(100*Gg)#�ɻ������Ũ��
    x=[Alpha_av,DeltaV,VH2O,Vg,rRO2,rH2O,r,Gg,mu]
    return x

def print_table_english():#���Ϊ��Ӣ��
    table = PrettyTable(["characteristics","unit","furnace","superheater","reheater","economizer","airheater"])  
    table.align= "r" # �Ҷ���
    table.padding_width = 1 # One space between column edges and contents (default)
      
    x0=["Alpha_av","DeltaV","VH2O","Vg","rRO2","rH2O","r","Gg","mu"]
    x1=['','Nm3/Kg','Nm3/Kg','Nm3/Kg','','','','Kg/Kg','Kg/Kg']
    x2=gas_characteristics(79.62,5.03,13.81,0.97,0.57,15,13,33.64,0.95,1.2)
    x3=gas_characteristics(79.62,5.03,13.81,0.97,0.57,15,13,33.64,0.95,1.22)
    x4=gas_characteristics(79.62,5.03,13.81,0.97,0.57,15,13,33.64,0.95,1.24)
    x5=gas_characteristics(79.62,5.03,13.81,0.97,0.57,15,13,33.64,0.95,1.26)
    x6=gas_characteristics(79.62,5.03,13.81,0.97,0.57,15,13,33.64,0.95,1.34)
  
    for i in range(0,9):
        table.add_row([x0[i], x1[i],"%.4f" % x2[i],"%.4f" % x3[i],"%.4f" % x4[i],"%.4f" % x5[i],"%.4f" % x6[i]])  
    print(table)  
print_table_english()