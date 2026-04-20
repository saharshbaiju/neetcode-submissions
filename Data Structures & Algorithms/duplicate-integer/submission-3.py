# Given an integer array nums, return true if any value appears more than once in the array,
#  otherwise return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen= set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False
        