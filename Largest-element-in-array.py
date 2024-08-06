import array

arr1=array.array('i', [6,1,4,2,3,6,9])


print(arr1)


def largest(arr):
    largest_ele= arr[0]

    for element in arr:
        if element > largest_ele:
            largest_ele=element
    return largest_ele

print(largest(arr1))