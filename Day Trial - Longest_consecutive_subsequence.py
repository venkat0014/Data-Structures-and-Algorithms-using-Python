#Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.


def longest_consecutive_subsequence(arr):
    if not arr:
        return 0

    # Convert the list to a set for O(1) lookups
    num_set = set(arr)
    longest_length = 0

    # Iterate through each number in the set
    for num in num_set:
        # Check if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Expand the sequence as long as consecutive numbers are found
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            # Update the longest sequence length if needed
            longest_length = max(longest_length, current_length)

    return longest_length

def main():
    # Test cases
    arr1 = [2, 6, 1, 9, 4, 5, 3]
    arr2 = [1, 9, 3, 10, 4, 20, 2]
    arr3 = [15, 13, 12, 14, 11, 10, 9]
    arr4 = [100, 4, 200, 1, 3, 2]

    # Calling the function and printing the results
    print("Test Case 1: ", longest_consecutive_subsequence(arr1))  # Output: 6
    print("Test Case 2: ", longest_consecutive_subsequence(arr2))  # Output: 4
    print("Test Case 3: ", longest_consecutive_subsequence(arr3))  # Output: 7
    print("Test Case 4: ", longest_consecutive_subsequence(arr4))  # Output: 4

if __name__ == "__main__":
    main()
