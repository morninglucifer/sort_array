def insertionsort(array):
    for i in range(1, len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key <array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
arr=[83,1,45,5,45,52,11,47,0,45,67,82]
insertionsort(arr)
print("sort array in ascending....", arr)
