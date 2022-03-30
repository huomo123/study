list1=['A','B','C','D','E','F']
list2=['B','A','E','G']
#按照list2的顺序排列list1

def sort(list1,list2):
    list3=[]
    for a in list2:
        if a in list1:
            list3.append(a)
            list1.remove(a)
    
    return list3+list1

a = sort(list1,list2)
print(a)

