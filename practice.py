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

    unique_words = set(words)

    return [word for word in unique_words]


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

    unique_items1 = set(items1)
    unique_items2 = set(items2)
    unique_common_items = set()

    for element_unique_items1 in unique_items1:
        for element_unique_items2 in unique_items2:
            if element_unique_items1 == element_unique_items2:
                unique_common_items.add(element_unique_items1)
                break # Once there is one match, we know that element is in
                # common and do not need to check for further matches.  Without
                # this `break`, the code works but less efficiently.

    return unique_common_items


    # Alternative solution:
    # We only need to make a set for one of two input lists to take advantage
    # of look-up in sets being faster than in lists (?).

    # unique_items2 = set(items2)
    # unique_common_items = set()

    # for element_items1 in items1:
    #     for element_unique_items2 in unique_items2:
    #         if element_items1 == element_unique_items2:
    #             unique_common_items.add(element_items1)
    #             break

    # return unique_common_items    


    # Alternative solution without making a set for any of the input lists 
    # first because as we make the resulting set, if we add a duplicate to the 
    # set, the set ignores the duplicate anyway.  However, we lose the benefit 
    # that look-up in sets is faster than in lists:

    # unique_common_items = set()

    # for element_items1 in items1:
    #     for element_items2 in items2:
    #         if element_items1 == element_items2:
    #             unique_common_items.add(element_items1)
    #             break

    # return unique_common_items


    # Alternative solution using set comprehension:
    # Unsure of formatting style

    # return set(element_items1 
    #             for element_items1 in items1 
    #             for element_items2 in items2 
    #             if element_items1 == element_items2)


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

    unique_numbers = set(numbers)
    pairs = []

    for num in unique_numbers:
        if num <= 0:
            if abs(num) in unique_numbers:
                if [num, abs(num)] not in pairs:
                    pairs.append([num, abs(num)])
    
    return pairs

    # Question: Is there a way to write this code using list comprehension?


    # Alternative solution if we do not let ourselves use `if ___ in ___` on 
    # sets:

    # unique_numbers = set(numbers)
    # pairs = []

    # for num1 in unique_numbers:
    #     if num1 <= 0:
    #         for num2 in unique_numbers:
    #             if abs(num1) == num2:
    #                 if [num1, num2] not in pairs:
    #                     pairs.append([num1, num2])
    
    # return pairs


    # Alternative solution if we do not let ourselves use `if ___ in ___` on 
    # sets and we check whether element is already in output list sooner:

    # unique_numbers = set(numbers)
    # pairs = []

    # for num1 in unique_numbers:
    #     if num1 <= 0 and [num1, abs(num1)] not in pairs:
    #         for num2 in unique_numbers:
    #             if abs(num1) == num2:
    #                 pairs.append([num1, num2])
    
    # return pairs


    # This solution does not work yet!  Work-in-progress alternative solution 
    # if we do not let ourselves use `if ___ in ___` on sets or on lists:

    # unique_numbers = set(numbers)
    # pairs = []

    # for num1 in unique_numbers:
    #     if num1 <= 0:
    #         for pair in pairs:
    #             if pair[0] == num1:
    #                 break
    #             for num2 in unique_numbers:
    #                 if abs(num1) == num2:
    #                     pairs.append([num1, num2])
    #     continue
    
    # return pairs


    # This solution does not work:

    # unique_numbers = set(numbers)
    # pairs_set = set()
    # pairs_list = []

    # for num in unique_numbers:
    #     if num <= 0:
    #         if abs(num) in unique_numbers:
    #             pairs_set.add([num, abs(num)]) # Wanting to take advantage of
    #             # sets ignoring additions that are duplicates, instead of
    #             # having the program check whether an element is in the
    #             # collection before deciding whether to add the element into
    #             # the collection.  However, this code gives 
    #             # `TypeError: unhashable type: 'list'` because we cannot add
    #             # elements that are mutable into a set. 

    # for pair in pairs_set:
    #     pairs_list.append(pair)
    
    # return pairs_list


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

    # char_counts = {}

    # for char in phrase:
    #     if char == " ":
    #         continue
    #     char_counts[char] = char_counts.get(char, 0) + 1
    
    # # Checking that dictionary is as we expect:
    # # print(char_counts)
    # # print(char_counts.get("T")) # Prints value
    # # print(char_counts.values()) # Prints list of values
    # # print(char_counts.items()) # Prints list of tuples

    # most_common_chars = []

    # for key, value in char_counts.items():
    #     if value == max(char_counts.values()):
    #         most_common_chars.append(key)

    # most_common_chars.sort()

    # return most_common_chars


    # Alternative solution using list comprehension:
    char_counts = {}

    for char in phrase:
        if char == " ":
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
    
    return sorted([key 
            for key, value in char_counts.items()
            if value == max(char_counts.values())])

    # Note: This code treats "T" and "t" as different characters, for example. 
    #  We could modify the program to make one key in our dictionary 
    # represent both "T" and "t".
    # Punctuation marks, such as "." and ",", can be in our dictionary. 


# top_chars("The rain in spain stays mainly in the plain.") # Testing

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    """ Print sorted list of pairs where the pairs are sorted."""
    # NOTE: This is used only for documentation tests. You can ignore it.

    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()
