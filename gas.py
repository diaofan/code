# coding=gbk
from prettytable import PrettyTable  

def gas_characteristics(Cdaf,Hdaf,Odaf,Ndaf,Sdaf,Aar,Mar,Vdaf,Alpha_fa,Alpha_av):#计算烟气特性
    Car=(100-Mar-Aar)/100*Cdaf#首先将干燥无灰基下的元素成分转换为收到基
    Har=(100-Mar-Aar)/100*Hdaf
    Oar=(100-Mar-Aar)/100*Odaf
    Nar=(100-Mar-Aar)/100*Ndaf
    Sar=(100-Mar-Aar)/100*Sdaf
    V0=1/0.21*(1.866*Car/100+5.56*Har/100+0.7*Sar/100-0.7*Oar/100)#理论空气量
    VRO2=1.866*(Car+0.375*Sar)/100#三原子容积
    V0H2O=0.111*Har+0.0124*Mar+0.0161*V0#理论水蒸气容积
    V0N2=0.79*V0+22.41/28*Nar/100#理论氮气容积
    V0g=VRO2+V0N2+V0H2O#理论烟气容积
    DeltaV=V0*(Alpha_av-1)#过剩空气量
    VH2O=V0H2O+0.0161*DeltaV#水蒸气容积
    Vg=VRO2+V0N2+DeltaV+VH2O#烟气总容积
    rRO2=VRO2/Vg#RO2气体占烟气容积份额
    rH2O=VH2O/Vg#水蒸气占烟气容积份额
    r=rRO2+rH2O#三元子气体和水蒸气占烟气容积份额之和
    Gg=1-Aar/100+1.306*Alpha_av*V0#烟气质量
    mu=Aar*Alpha_fa/(100*Gg)#飞灰无因次浓度
    x=[Alpha_av,DeltaV,VH2O,Vg,rRO2,rH2O,r,Gg,mu]
    return x

def print_table_english():#表格为纯英文
    table = PrettyTable(["characteristics","unit","furnace","superheater","reheater","economizer","airheater"])  
    table.align= "r" # 右对齐
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