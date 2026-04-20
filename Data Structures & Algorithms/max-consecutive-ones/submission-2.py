class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            cnt += 1 if i else -cnt
            res=max(res,cnt)
        return res