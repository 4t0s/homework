# array=[1,5,4,3,2]
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[1]>arr[j+1]:
#                 arr[j], arr[j+1]=arr[j+1], arr[j]

# bubble_sort(array)
def bubbleSort( theSeq ):
    n = len( theSeq )

    for i in range( n - 1 ) :
        flag = 0

        for j in range(n - 1) :
            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return theSeq


array=[1,2,-9]

def IsAscending(array):
    IsRight = 0
    new_array=bubbleSort(array)
    for i in range(len(new_array)):
        if array[i]==new_array[i]:
            IsRight += 1
        else:
            IsRight -= 100
    if IsRight == len(array):
        print('YES')
    else:
        print('NO')
IsAscending(array)