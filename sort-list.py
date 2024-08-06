
#simple linear sort

def sort_list(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i]>list[j]:
                list[i],list[j]= list[j],list[i]

    return list

list=[6,5,8,1,3,9,23,4,5,8]

print(sort_list(list))