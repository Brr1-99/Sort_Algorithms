
"""
BubbleSort Algorithm:

    Inner Loop:
    - Start by checking the first and second digit
    - Put the greater value on the right by swapping if necessary
    - Now do the same for the second and third digit
    - Continue till the end of the array
    - Each time we enter the inner loop the number of iterations decreases by one
    as we at least sort one digit each time 

    Outer Loop:
    - Repeat the inner loop (length of the list - 1) times exiting the loop if isSorted is True.
    - Time complexity can go from O(n), array already sorted, to O(n^2), reverse sorted array.
"""

def BubbleSort(arr: list[int]) -> list[int]:
    for i in range(0, len(arr)):
        isSorted = True
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                isSorted = False
        if isSorted:
            break
    return arr

"""
InsertionSort Algorithm:

    Inner Loop:
    - Start by checking the second digit
    - Put the smaller value on the left by swapping if necessary
    - Continue with the third value and each time we create a new sorted array
    - Each time we enter the inner loop the number of iterations increases by one
    as we are growing our 'sorted' array always by one

    Outer Loop:
    - Repeat the inner loop (length of the list - 1) times exiting the loop if isSorted is True.
    - Time complexity is O(n^2).
    - Only used for small sets of data
"""

def InsertionSort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        j = i-1
        while arr[j] > arr[j+1] and j >= 0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr

"""
MergeSort Algorithm:

    Break list in half until we have lists of one value, which is sorted already
    We merge consecutive pair of one-item list and sort them
    We continue going backwards sorting the lists from smaller to bigger ones

    Recursive algorithm
    Very efficient for large amounts of data
    Time complexity of O(n log n)

"""

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) > 1 :
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

"""
QuickSort Algorithm

    Choose a pivot number from the list, normally the median from first, middle and last values
    Place it on the start of the array
    Now we iterate over the array and separate values which are smaller than the pivot and greater than the pivot
    The pivot stays at the middle of both groups so its already sorted
    We continue doing this for the smaller groups


    Recursive algorithm
    Time complexity of O(n log n)
"""

def quick_sort(arr: list[int], left: int, right: int) -> list[int]:
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)
    return arr

def partition(arr: list[int], left: int, right: int) -> int:
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] <= pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i
    
print(quick_sort([4,6,2,3,1,2,3,5,6], 0, 8))