from main import merge_sort

def test_bubble_sort() -> None:
    sorted_array = merge_sort([6, 4, 2, 5, 3, 1])
    assert sorted_array == [1, 2, 3, 4, 5, 6]