qzh= 0,31,59,90,120,151,181,212,243,273,304,334,365
def is_leap_year(y):
    if y%4==0 and y%100 or y%400==0:
        return True
    return False
y = int(input("请输入年份>>"))
m = int(input("请输入月份>>"))
s = '================[{:>10d}/{:<10d}]================\n  周日\t  周一\t  周二\t  周三\t  周四\t  周五\t  周六\n'.format(y,m)
wd = ((y-1)*365+(y-1)//4-(y-1)//100+(y-1)//400+qzh[m-1]+(is_leap_year(y) and m>2)+1)%7
for i in range(0,wd):
    s+=' \t'
dim = qzh[m]-qzh[m-1]+(is_leap_year(y) and m==2)
for i in range(1,dim+1):
    if (i+wd)%7==0:
        s+='[{:^5d}]\n'.format(i)
    else:
        s+='[{:^5d}]\t'.format(i)  
print(s)
