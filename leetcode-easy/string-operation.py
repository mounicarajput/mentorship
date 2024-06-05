#https://leetcode.com/problems/find-common-characters/

"""Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order
Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]"""

#Solution
def common_characters(words):
    # Convert the first word into a set of characters
    common_chars = set(words[0])

    # Iterate through the rest of the words
    for word in words[1:]:
        # Take the intersection with each word's set of characters
        common_chars &= set(word)

    # Return the common characters as a list
    return list(common_chars)


# Example usage:
words = ["bella", "label", "roller"]
print(common_characters(words))

words = ["cool","lock","cook"]
print(common_characters(words))