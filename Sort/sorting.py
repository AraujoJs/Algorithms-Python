def selection_sort(list):
    n = len(list)
    for i in range(0, n-1):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

def bubble_sort(list):
    n = len(list)
    for j in range(0, n-1):
        for i in range(0, n-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        return list

def quick_sort(list, begin=0, end=None):
    if end is None:
        end = len(list)-1
    if begin < end:
        p = partition(list, begin, end)
        quick_sort(list, begin, p-1)
        quick_sort(list, p+1, end)
    return list

def partition(list, begin, end):
    pivot = list[end]
    i = begin
    for j in range(begin, end):
        if list[j] < pivot:
            list[i], list[j] = list[j], list[i]
            i = i + 1
    list[i], list[end] = list[end], list[i]
    return i
