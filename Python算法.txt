算法：
一、九九乘法表：
for a in range(1,10):
    for b in range(1,a+1):
        print(str(a)+'x'+str(b)+'='+str(a*b)+'\t',end='') 
    print() 
------------------------------------
二、阶乘循环：
def A(n):
    num=1
    for i in range(1,n+1):
        num=i*num
    return num
阶乘递归：
def B(n):
    if n==1:
        return 1
    else:
        return n*B(n-1)
------------------------------------
三、走楼梯：可走1、2、3步
m为楼梯层数
def C(m):
    if m==1:
        return 1
    elif m==2:
        return 2
    elif m==3:
        return 4
    else:
        return C(m-1)+C(m-2)+C(m-3)
------------------------------------
四、二分法查找列表中数字：
def D(list1,f):
    len1=len(list1)
    if len1==0:
        print('未找到')
        return False
    mid=len1//2
    if list1[mid]>f:
        print(list1[:mid])
        return D(list1[:mid],f)
    elif list1[mid]<f:
        print(list1[mid+1:])
        return D(list1[mid+1:],f)
    else:
        print('找到',str(f))
------------------------------------
五、列表区分奇偶数
list1=[]
even=[]
odd=[]
while len(numbers)>0
    number=list1.pop()
    if(numbers%2==0):
        even.append(number)
    else
        odd.append(number)