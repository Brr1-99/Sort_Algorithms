
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

print(InsertionSort([4,6,2,3,1,2,3,5,6]))