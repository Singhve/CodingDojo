def selectionSort(arrList):
    for i in range(len(arrList)-1):
        min = i
        for j in range(i+1,len(arrList)):
            if arrList[min] > arrList[j]:
                min = j
        arrList[i],arrList[min] = arrList[min],arrList[i]
    return arrList

print(selectionSort([7,6,3,2,9,0,1,5,8]))

def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        minimum = i
        for j in range(i+1, n):
            if (array[j] < array[minimum]):
                minimum = j
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array

print(selectionSort([7,6,3,2,9,0,1,5,8]))