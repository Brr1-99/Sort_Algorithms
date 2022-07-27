
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


print(BubbleSort([1,2,3,5,6]))