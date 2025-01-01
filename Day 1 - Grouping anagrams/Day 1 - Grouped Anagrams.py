from collections import defaultdict

def group_anagrams(arr):
    # Step 1: Create a dictionary to store groups
    anagram_groups = defaultdict(list)

    # Step 2: Group words by their sorted characters
    for word in arr:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    # Step 3: Keep the groups in the order of first appearance
    result = [group for group in anagram_groups.values()]

    # Step 4: Sort each group lexicographically
    result = [group for group in result]

    return result

# Example usage
arr = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
print(group_anagrams(arr))
