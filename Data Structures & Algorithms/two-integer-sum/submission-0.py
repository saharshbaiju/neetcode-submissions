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

            
            