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