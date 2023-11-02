def bubble_sort(arr):
    n = len(arr)  # Determine array length.
    
    # Outer loop: Passes through the array.
    for i in range(n - 1):
        
        # Inner loop: Compares elements.
        for j in range(n - i - 1):
            
            # Swap if current element is greater than next.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    # Return the sorted array.
    return arr

# Sample array.

array = [5, 2, 3, 1, 4]
print("Unsorted array: ", array)

# Sort the array using bubble_sort.
sorted_array = bubble_sort(array)

# Display sorted array.
print("Sorted array: ", sorted_array)
