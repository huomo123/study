查看URL返回：
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'url')
print(r.status)
print(r.data)
------------------------------------
返回json：
import json
r = http.request('GET', 'url')
print(json.loads(r.data.decode('utf-8')))
------------------------------------
网络请求：
import requests
r=requests.post(url,data)
print(r)
print(r.text)
------------------------------------
两个列表对应相加：
list3=[]
for i in range(len(list1)):
    a=list1[i]+list2[i]
    list3.append(a)
------------------------------------
Python输出txt文件内第二列：
for line in open('*.txt'):
    ll=line.strip(),split(',')
    print(ll[1])
strip() --去掉首尾空格回车
split(',') --以逗号为分隔符
------------------------------------
字典输出value值并生成列表：
list=[]
for a in dict.values():
    list.append(a)
------------------------------------
两个字典匹配key值输出对应value值并相加：
for key,value in dict1.items():
    dict1[key]=value+dict2[key]