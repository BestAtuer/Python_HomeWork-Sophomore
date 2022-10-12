#Author: Atuer
import math as M
days_qzh= [0,31,59,90,120,151,181,212,243,273,304,334,365]
# 判断今年是否为闰年
def is_leap_year(y):
    if (y%4==0 and y%100) or y%400==0:
        return True
    return False
# 今年此月前日期数
def days_before(y,m):
    return (y-1)*365+M.floor((y-1)/4)-M.floor((y-1)/100)+M.floor((y-1)/400)+days_qzh[m-1]+(is_leap_year(y) and m>2)
# 本月日期数
def days_in_month(y,m):
    return days_qzh[m]-days_qzh[m-1]+(is_leap_year(y) and m==2)
#主程序
y = int(input("请输入年份>>"))
m = int(input("请输入月份>>"))
s = '================[{:>10d}/{:<10d}]================\n'.format(y,m)+ "  周日\t  周一\t  周二\t  周三\t  周四\t  周五\t  周六\n"
wd = (days_before(y,m)+1)%7
for i in range(0,wd):
    s+=' \t'
dim = days_in_month(y,m)
for i in range(1,dim+1):
    if (i+wd)%7==0:
        s+='[{:^5d}]\n'.format(i)
    else:
        s+='[{:^5d}]\t'.format(i)  
print(s)
