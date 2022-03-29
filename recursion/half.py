
# 四、二分法查找列表中数字：
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

list1 = [1,2,3,5,6,7,9]
search = 7
D(list1, search)