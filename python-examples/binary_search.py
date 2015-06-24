""" An example of the binary search algorithm in python.
	Binary search depends on the given array ( or list in python terms)
	already being sorted.

	The code is liberally sprinkled with obvious comments as this
	is intended to be a simple demonstration/tutorial example
	of a popular and useful algorithm. Python's an excellent
	language for showing simple algorithms to beginner/intermediate
	developers.
"""

import unittest

def binary_search(alist, item):
	"""Perform a binary search on alist, searching for item.
	"""
	if not isinstance(alist, list):
		raise ValueError('Please input a list of numbers.')

	# Create the upper and lower bounds of the list,
	# ie the maximum and minimum values.
	lower = 0
	upper = len(alist) - 1

	found = False

	while lower <= upper and not found:
		# Pick a pivot point (or midpoint) to use;
		# we'll divide the list by two to find the initial
		# midpoint.
		pivot = (lower + upper) // 2

		if alist[pivot] == item:
			# If the inital pivot point happens to be the item we're
			# searching for, no more work needs to be done.
			found = True
		else:
			if item < alist[pivot]:
				# If the pivot point is bigger than the item we're
				# searching for, the item must be on the lower half
				# of the list.
				# So, we adjust the maximum value to be one less than
				# the original pivot point. lower can remain the same
				# since we're using the lower (first) half of the list.
				upper = pivot - 1
			else:
				# Likewise, if the pivot point is smaller than the item we're
				# searching for, it must be on the upper half of the list.
				# We can keep the maximum value, and simply change the
				# variable that defines the start of the list to be one more
				# than the original pivot point.
				lower = pivot + 1
	# This will keep searching, narrowing the list down into smaller
	# and smaller halves, for every iteration of the while loop.
	# Eventually the pivot point will be equal to the item we're
	# searching for, and we can change our *found* variable to True.
	# The recursive nature of the search is what makes this a
	# 'divide and conquer' algorithm.
	return found


# Test.
class TestBinarySearch(unittest.TestCase):


	"""Test our method succeeds and fails when it should."""

	def test_search(self):
		my_list = [a for a in range(1, 11)]
		self.assertEqual(binary_search(my_list, 5), True)

	def test_search_fails_with_bad_input(self):
		with self.assertRaises(ValueError):
			binary_search('hello world', 5)

if __name__ == '__main__':
	unittest.main()


