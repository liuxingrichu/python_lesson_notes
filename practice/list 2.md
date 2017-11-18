£¨1£©Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) ¡ú 6

sum13([1, 1]) ¡ú 2

sum13([1, 2, 2, 1, 13]) ¡ú 6

´ð°¸£º
def sum13(nums):
    new_nums = list()
    flag = False
    for i in range(len(nums)):
        if flag:
            flag = False
            continue
        if nums[i] is not 13:
            new_nums.append(nums[i])
        else:
            if i+1 is not len(nums):
                flag = True
            else:
                break
    return sum(new_nums)
	
£¨2£©Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) ¡ú True

has22([1, 2, 1, 2]) ¡ú False

has22([2, 1, 2]) ¡ú False	

´ð°¸£º
def has22(nums):
  while nums.count(2) > 1:
    position = nums.index(2)
    if nums[position + 1] is 2:
        return True
    else:
        del nums[position]
  else:
    return False
		