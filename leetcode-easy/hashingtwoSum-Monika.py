#For efficient solution, you can use a hash map (also known as a dictionary in Python) to a
# chieve a time complexity of O(n). Here's the code:

#Question Link: https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    num_dict = {}  # Create an empty dictionary to store numbers and their indices

    for i, num in enumerate(nums):  # Loop through each number and its index
        extpected_number = target - num  # Calculate the number needed to reach the target

        if extpected_number in num_dict:  # Check if the complement is already in the dictionary
            return [num_dict[extpected_number], i]  # If found, return the indices

        num_dict[num] = i  # Otherwise, add the current number and its index to the dictionary

    return None  # If no pair is found, return None

# Using the function with your example:
nums = [2, 7, 11, 15]
target = 17
result = twoSum(nums, target)
print(result)



"""
Additional Notes:

In Python, enumerate is a built-in function that adds a counter to an 
iterable object (like a list) and returns it in a form of enumerate object. 
This allows you to loop over the elements of the iterable while also having access to their index or position.

For example, if you have a list ['apple', 'banana', 'cherry'], 
using enumerate will give you something like this:

0, 'apple'
1, 'banana'
2, 'cherry'

"""

"""
Logic:

So, when extpected_number in num_dict is true, 
it means that we've found a pair of numbers (one in the list, and 
one that's needed to reach the target). Here's how it works:

Let's say we're at the first iteration of the loop, where num is 2. The complement is 7.

The code checks if 7 is in num_dict. If it is, it means that we've already seen a number 
earlier in the list that can be added to the current number to reach the target.

If it's true, then num_dict[extpected_number] gives us the index of the extpected_number. 
In this case, num_dict[7] would return the index where 7 was first found in the list.

i is the index of the current number in the loop. So, i gives us the index of the current number.

The return [num_dict[extpected_number], i] line then creates a list with these two indices: [num_dict[extpected_number], i]. 
This list is returned as the output of the function.

This is how the function is able to find the indices of two numbers 
that add up to the target. If it doesn't find a pair, it continues with the loop, 
and if no pair is found at all, it eventually returns None.


"""
