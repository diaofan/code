'''
Created on 2016年6月10日

@author: diaofan
'''
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import math
import xlrd
from  statistics import mean,stdev,pstdev,variance,pvariance

from prettytable import PrettyTable

def getData(filename):
    excel = xlrd.open_workbook(filename)
    sheet = excel.sheets()[0]     #获取第一个sheet
    ncols = sheet.ncols #列数
    nrows = sheet.nrows #行数
    x_data = 0
    y_data = 0
    xygroups=[]
    xy={'x':[],'y':[]}

    for i in range(0,ncols,2):
        for j in range(0,nrows):
            x_data = sheet.cell_value(j,i)
            y_data = sheet.cell_value(j ,i + 1)

            xy['x'].append(float(x_data))
            xy['y'].append(float(y_data))


        xygroups.append(xy)
        xy={'x':[],'y':[]}



    return xygroups


def staData(x,y):
    xsta={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None}
    ysta={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None}

    xsta['avg']=mean(x)
    ysta['avg']=mean(y)

    xsta['stdev']=stdev(x)
    ysta['stdev']=stdev(y)

    xsta['pstdev']=pstdev(x)
    ysta['pstdev']=pstdev(y)

    xsta['var']=variance(x)
    ysta['var']=variance(y)

    xsta['pvar']=pvariance(x)
    ysta['pvar']=pvariance(y)

    r=np.corrcoef(x,y)[0, 1]

    return  xsta,ysta,r

def plot(xygroups):

    figcount=len(xygroups)
    figcol=2
    figrow=math.ceil(figcount/figcol)
    fig=plt.figure(figsize=(12.0,8.0))
    fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)

    for i in range(0,len(xygroups)):
        a,b = np.polyfit(xygroups[i]['x'],xygroups[i]['y'],1)
        predictedY = a*np.array(xygroups[i]['x']) + b
        fig.add_subplot(figrow, figcol,i+1)     #子图
        plt.plot(xygroups[i]['x'],xygroups[i]['y'], 'bo')

        plt.title("Group "+str(i+1))
        plt.xlabel('x')
        plt.ylabel('y')

        plt.plot(xygroups[i]['x'],predictedY,
                   label = 'Y by\nlinear fit, y = '
                   + str(round(a, 5))+'*x+'+str(round(b, 5)))

        plt.legend(loc = 'best')

def draw_table(xygroups):
    table = PrettyTable(["data set",
                         "x-avg", "x-std", "x-pstd", "x-var","x-pvar",
                         "y-avg", "y-std", "y-pstd", "y-var","y-pvar",
                         "pearson_r"])
    for i in range(len(xygroups)):
        xsta,ysta,r=staData(xygroups[i]['x'], xygroups[i]['y'])

        table.add_row(["file" "%.0f" % i,
                   "%.3f" % xsta['avg'],
                   "%.3f" % xsta['stdev'],"%.3f" %xsta['pstdev'],
                   "%.3f" % xsta['var'],"%.3f" % xsta['pvar'],
                   "%.3f" % ysta['avg'],
                   "%.3f" % ysta['stdev'],"%.3f" % ysta['pstdev'],
                   "%.3f" % ysta['var'],"%.3f" % ysta['pvar'],
                   "%.3f" % r])
    return table



xygroups = getData('data6.xlsx')
print(draw_table(xygroups))
plot(xygroups)
plt.show()

