# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum=0
        
        loop = True
        i=j=0

        while loop:

            if nums[i] + nums[j] == target and i!=j:
                return [i,j]

            elif j == (len(nums)-1):
                i+=1
                j=-1
            
            if i== (len(nums)-1):
                break
            j+=1

            
            