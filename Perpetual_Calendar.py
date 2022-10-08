#核心代码共30行 Author: Atuer
import math as M
days= [31,28,31,30,31,30,31,31,30,31,30,31]
#判断闰年
def is_leap_year(y):
    if (y%4==0 and y%100) or y%400==0:
        return True
    return False
#今年前总日子数
def days_before_year(y):
    return (y-1)*365+M.floor((y-1)/4)-M.floor((y-1)/100)+M.floor((y-1)/400)
#本月总日子数
def days_in_month(y,m):
    if is_leap_year(y) and m==2:
        return 29
    return days[m-1]
#今年次月前总日子数
def days_before_month(y,m):
    sum = int(0)
    for i in range(1,m):
        sum+=days_in_month(y,i)
    return sum
#主程序
while True:
    y = int(input())
    m = int(input())
    #非法判断
    if (not y) and (not m):
        break
    elif m>12 or m<1:
        print("非法月份")
    #核心代码
    else:
        wd = (days_before_year(y)+days_before_month(y,m)+1)%7
        dim = days_in_month(y,m)+1
        s = '================[{:>10d}/{:<10d}]================\n'.format(y,m)+ "  周日\t  周一\t  周二\t  周三\t  周四\t  周五\t  周六\n"
        for i in range(0,wd):
            s+=' \t'
        for i in range(1,dim):
            if (i+wd)%7==0:
                s+='[{:^5d}]\n'.format(i)
            else:
                s+='[{:^5d}]\t'.format(i)  
        print(s)
