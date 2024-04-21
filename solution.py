def minimized_ordering_time(wafers):
    # Sorting wafers based on Johnson's rule:
    # Each wafer is a tuple (machine1_time, machine2_time, wafer_id)
    
    # Sorting by the minimum time of either machine to determine processing order.
    # You can sort with this "sorted_wafers = sorted(wafers, key=lambda x: min(x[0], x[1]))" or manually using merge sort. Both of them give the same time complexity
    sorted_wafers = merge_sort_wafers(wafers)
    
    # Initialize lists to separate wafers for optimal processing order.
    first_half = []
    second_half = []
    # Loop through sorted wafers to assign them to first_half or second_half.
    for wafer in sorted_wafers:
        if wafer[0] < wafer[1]:
            first_half.append(wafer)  # Wafer goes early if Machine 1 time is less.
        else:
            second_half.append(wafer)  # Wafer goes late if Machine 2 time is less.
    second_half.reverse()  # Reverse second_half to process these last.

    # Combine the two halves to form the optimal processing sequence.
    optimal_sequence = first_half + second_half
    
    # Initialize timing metrics.
    current_time = 0
    machine1_time = 0
    machine2_time = 0
    # Calculate processing times for each wafer in the optimal sequence.
    for wafer in optimal_sequence:
        start_time_m1 = current_time
        finish_time_m1 = start_time_m1 + wafer[0]
        machine1_time = finish_time_m1
        
        start_time_m2 = max(finish_time_m1, machine2_time)
        finish_time_m2 = start_time_m2 + wafer[1]
        machine2_time = finish_time_m2
        
        current_time = finish_time_m1  # Update current time for Machine 1

    # Compute total elapsed and idle times.
    total_elapsed_time = machine2_time
    idle_time_machine1 = machine2_time - machine1_time
    
    # Print results
    print("Wafer sequence:", [wafer[2] for wafer in optimal_sequence])
    print("Total elapsed time:", total_elapsed_time, "seconds")
    # This wasn't asked but just wanted to be thorough.
    print("Idle time on Machine 1:", idle_time_machine1, "seconds") 
    print('----------------------------------------------------------------------')
    
    # Complexity Analysis
    # Sorting takes a time complexity of O(nlogn). The remaining steps (splitting the list, reversing a list, and simulating the processing of wafers) has a linear time complexity of O(n) each.
    print("Time Complexity: O(nlogn)")
    # The space complexity of the algorithm is primarily O(n), needed to store the sorted wafers and the additional structures for the two halves and the optimal sequence. 
    print("Space Complexity: O(n)")


def merge_sort_wafers(wafers):
    """
    Sorts a list of wafers using the merge sort algorithm based on the minimum processing time
    of two machines.

    Parameters:
    - wafers: List of tuples, where each tuple is (machine1_time, machine2_time, wafer_id)

    Returns:
    - List of tuples sorted by the minimum processing time across two machines.
    """

    # Base case: A list of zero or one wafer is already sorted
    if len(wafers) <= 1:
        return wafers

    # Recursive case: Split the list into two halves
    mid_point = len(wafers) // 2
    left_half = wafers[:mid_point]
    right_half = wafers[mid_point:]

    # Recursively sort both halves
    left_sorted = merge_sort_wafers(left_half)
    right_sorted = merge_sort_wafers(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list based on the minimum processing time.

    Parameters:
    - left: The sorted left half of wafers.
    - right: The sorted right half of wafers.

    Returns:
    - A merged and sorted list of wafers.
    """
    sorted_list = []
    left_index, right_index = 0, 0

    # Traverse both lists and append the smaller element to the sorted list
    while left_index < len(left) and right_index < len(right):
        if min(left[left_index][0], left[left_index][1]) < min(right[right_index][0], right[right_index][1]):
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # If there are remaining elements in either left or right, append them
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list
   
    

# Start of the main program execution: asks user for input choice.
choice = input("Do you want to enter input on your own (type 'own') or test a sample case (type 'sample')? ")
print('----------------------------------------------------------------------')
if choice.lower() == 'sample':
    # Use a sample set of wafers if the user selects "sample".
    print("Sample Input:")
    print("n = 2")
    wafers = [(5, 8, 'w1'), (2, 7, 'w2'), (3, 4, 'w3')]
    print("t =", wafers)
    print('----------------------------------------------------------------------')
    minimized_ordering_time(wafers)
elif choice.lower() == 'own':
    # Allow user to input their own wafer processing times if they choose "own".
    wafers = []
    n = int(input("How many wafers? "))
    for i in range(n):
        m1_time = int(input(f"Enter Machine 1 processing time for wafer {i+1}: "))
        m2_time = int(input(f"Enter Machine 2 processing time for wafer {i+1}: "))
        wafers.append((m1_time, m2_time, f'w{i+1}'))
    print('----------------------------------------------------------------------')
    minimized_ordering_time(wafers)
else:
    # Handle invalid input.
    print("Invalid input. Exiting program.")
