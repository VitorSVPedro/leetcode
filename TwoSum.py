class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lt = len(nums)
        for n in range(lt):
            for nr in range(n+1, lt):
                if nums[n]+nums[nr]==target:
                    return(n, nr)