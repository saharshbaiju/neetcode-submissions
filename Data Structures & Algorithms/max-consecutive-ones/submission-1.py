class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        mcnt = 0
        cnt = 0

        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1

            
            else:
                if cnt> mcnt :
                    mcnt = cnt
                cnt = 0

            if i == (len(nums)-1):
                    if cnt> mcnt:
                        mcnt = cnt

        return mcnt