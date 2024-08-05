#given a nested list, convert the list to flat list


input=x = [1, 2, [3, 4, [5], [6, 7]], 7, [8, 9]]

output=[]
def flatten_list(input):
    for element in input:
        if isinstance(element,list):
            flatten_list(element)
        else:
            output.append(element)
    return output

print(flatten_list(input))
