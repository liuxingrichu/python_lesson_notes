（1）Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

first_last6([1, 2, 6]) → True

first_last6([6, 1, 2, 3]) → True

first_last6([13, 6, 1, 2, 3]) → False

答案：
def first_last6(nums):
  return (nums[0]==6 or nums[-1]== 6)
  
（2）Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False

same_first_last([1, 2, 3, 1]) → True

same_first_last([1, 2, 1]) → True

答案：
def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[-1])
  
（3）Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

make_pi() → [3, 1, 4]

答案：
def make_pi():
  return [3, 1, 4]

（4）Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]

max_end3([11, 5, 9]) → [11, 11, 11]

max_end3([2, 11, 3]) → [3, 3, 3]

答案：
def max_end3(nums):
  num = nums[0] if nums[0] >= nums[-1] else nums[-1]
  return [num for i in range(3)]
  
（5）Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]

reverse3([5, 11, 9]) → [9, 11, 5]

reverse3([7, 0, 0]) → [0, 0, 7]  

答案：
def reverse3(nums):
  nums.reverse()
  return nums
  
（6）Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

make_ends([1, 2, 3]) → [1, 3]

make_ends([1, 2, 3, 4]) → [1, 4]

make_ends([7, 4, 6, 2]) → [7, 2]

答案：
def make_ends(nums):
    return [nums[0], nums[-1]]
	
