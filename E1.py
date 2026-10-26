def linear_search(arr, target):
    """
    Linear Search: Sequentially checks each element in the list.
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return True, i
    return False, -1

def binary_search(arr, target):
    """
    Binary Search: Repeatedly divides a sorted list in half.
    Time Complexity: O(log n) | Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False, -1

# --- Test Script for Assignment 1 ---
if __name__ == "__main__":
    print("=== EXPERIMENT 1: SEARCHING ALGORITHMS TEST ===")
    
    test_cases = [
        ([105, 210, 501, 302, 150, 702, 321], 302, "Found"),
        ([105, 210, 501, 302, 150, 702, 321], 700, "Not Found"),
        ([10, 20, 30, 40, 50], 10, "Found"),
        ([5, 15, 25, 35, 45], 45, "Found"),
        ([2, 4, 6, 8, 10], 7, "Not Found")
    ]
    
    for idx, (ids, target, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {idx}:")
        print(f"Input IDs: {ids}")
        print(f"Search ID: {target}")
        
        # 1. Linear Search
        lin_found, lin_idx = linear_search(ids, target)
        print(f"  - Linear Search Result: {'Found' if lin_found else 'Not Found'} (Index: {lin_idx})")
        
        # 2. Binary Search (Requires sorted array)
        sorted_ids = sorted(ids)
        bin_found, bin_idx = binary_search(sorted_ids, target)
        print(f"  - Binary Search (on sorted {sorted_ids}): {'Found' if bin_found else 'Not Found'} (Index: {bin_idx})")