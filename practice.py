"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example:

        >>> no_dupes = without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"])

        >>> isinstance(no_dupes, list)
        True

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]

    The function should return a variable of type list:
        >>> type(without_duplicates([111111, 2, 33333, 2]))
        <class 'list'>
    """
    # This will turn words, originally a list, into a set. I chose this because sets remove all duplicates.
    no_dupes = set(words)
    # I then turn the no_dupes set back into a list.
    return list(no_dupes)
# input is a list of words with duplicates
# Output is a list of words with duplicates removed
# Use integers as well
# Manual test:
# words = (['I', 'I', 'have', 'have', 2, 2, 'beautiful', 'beautiful', 'dogs', 'dogs', 'and', 'and', 'their', 'their', 'names', 'names', 'are', 'are', 'Achilles', 'Achilles', 'and', 'and', 'Athena', 'Athena'])
# result = without_duplicates(words)
# print(result)

def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a set of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should return a set:

        >>> unique_common_items = find_unique_common_items([1, 2, 3, 4], [2, 1])
        >>> isinstance(unique_common_items, set)
        True

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once:

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types:

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    # .intersection is used to find similar items from two different lists. 
    both_puppers = set(items1).intersection(items2)
    return (both_puppers)

    return set()

# items1 = (['Athena', 'is', 'black', 'big', 'cute', 'moody', 'loving', 'cuddly'])
# items2 = (['Achilles', 'is', 'black', 'smoll', 'cute', 'hyper', 'loving', 'cuddly'])
# both_puppers = find_unique_common_items(items1, items2)
# print(both_puppers)

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    zero_pairs = []

    # The code below won't work because it creates double pairs.
    # Each double pair shows the positive and negative integer together, 
    # then the negative and positive integer next.
    # This is the output: [(-5, 5), (5, -5), (2, -2), (-2, 2), (5, -5), (2, -2), (4, -4), (-4, 4)]
    # for num in numbers:
    #     negative_nums = -num
    #     if negative_nums in unique_nums:
    #         zero_pairs.append((num, negative_nums))

    # This will loop over the range of the length of the numbers set
    for i in range(len(numbers)):
        # This iterates over the indices starting from i + 1 to avoid counting pairs twice (which was a problem)
        # In the previous for loop
        for j in range(i + 1, len(numbers)):
            num_i = list(numbers)[i]
            num_j = list(numbers)[j]
            if num_i + num_j == 0:
                pair = sorted([num_i, num_j])  # Sort the pair to ensure uniqueness
                if pair not in zero_pairs:
                    zero_pairs.append(pair)

    # I kept getting a test failure because the zero was not adding another zero. This 
    # for loop was the solution
    for num in numbers:
        if num == 0:
            zero_pairs.append([0, 0])

    return zero_pairs

# Manual test:
# numbers = ([-5, 7, 5, 2, -2, 5, 3, 2, 4, -4, 12, 0])
# zero_num = get_sum_zero_pairs(numbers)
# print(zero_num)

def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    # Create an empty list
    char_counts = {}
    # This will iterate over the phrase 
    for char in phrase:
        if char != ' ':  # This ignores the spaces. It's saying if char doesn't equal a space then...
            # This populates the empty list with characters. The .get method will get a character
            # and as the program iterates over the string, will add 1 to inventory of characters if
            # it comes across it again.
            char_counts[char] = char_counts.get(char, 0) + 1 
    # If I return the function here, it will create a dictionary with the key as the letter and the value
    # as the number of times that letter occured in the string:
    # {'B': 1, 'e': 8, 'c': 3, 'a': 4, 'r': 4....}

    # This will show the max occurrence but will not show which letter if max_count is returned
    max_count = max(char_counts.values(), default=0)

    # Create a list of characters with the maximum occurrence count
    # char_counts.items iterates over the items (key-value pairs) in 
    # the char_counts dictionary. Each item is a tuple (char, count) where char 
    # is a character, and count is the count of occurrences of that character.
    most_common_chars = [char for char, count in char_counts.items() if count == max_count]

    # Sort the list alphabetically
    # most_common_chars.sort()

    # return most_common_chars
    return most_common_chars


phrase = ("Be careful with each other so you can be dangerous together.")
result = top_chars(phrase)
print(result)
#####################################################################
# You can ignore everything below this.


# def sort_pairs(l):
#     """ Print sorted list of pairs where the pairs are sorted."""
#     # NOTE: This is used only for documentation tests. You can ignore it.

#     return sorted(sorted(pair) for pair in l)


# if __name__ == "__main__":
#     print()
#     import doctest
#     if doctest.testmod().failed == 0:
#         print("*** ALL TESTS PASSED ***")
#     print()
