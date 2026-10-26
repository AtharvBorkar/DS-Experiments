def selection_sort(arr):
    """
    Selection Sort: Repeatedly selects the minimum element and places it at the beginning.
    Time Complexity: O(n^2) | Space Complexity: O(1)
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly compares and swaps adjacent elements.
    Time Complexity: O(n^2) | Space Complexity: O(1)
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def get_top_five(sorted_arr):
    """
    Retrieves the top 5 highest salaries from an ascending sorted list.
    (Highest salaries are located at the end of an ascending sorted list).
    """
    return sorted_arr[-1:-6:-1] if len(sorted_arr) >= 5 else sorted_arr[::-1]

# --- Test Script for Assignment 2 ---
if __name__ == "__main__":
    print("\n=== EXPERIMENT 2: SORTING ALGORITHMS & TOP 5 SALARIES TEST ===")
    
    test_cases_salaries = [
        [45000.50, 52000.75, 31000.00, 60000.25, 47000.80, 72000.10, 39000.45],
        [10000.0, 25000.0, 15000.0, 5000.0, 8000.0]
    ]
    
    for idx, salaries in enumerate(test_cases_salaries, 1):
        print(f"\nTest Case {idx}:")
        print(f"Original Salaries: {salaries}")
        
        # Test Selection Sort
        sel_sorted = selection_sort(salaries)
        print(f"  - Selection Sort (Ascending): {sel_sorted}")
        print(f"  - Top 5 Salaries: {get_top_five(sel_sorted)}")
        
        # Test Bubble Sort
        bub_sorted = bubble_sort(salaries)
        print(f"  - Bubble Sort (Ascending): {bub_sorted}")
        print(f"  - Top 5 Salaries: {get_top_five(bub_sorted)}")