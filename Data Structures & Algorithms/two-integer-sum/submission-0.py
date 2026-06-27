class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {nums[0]: 0}
        for i in range(1, len(nums)):
            if (target-nums[i]) in tracker:
                return [tracker[(target-nums[i])], i]
            tracker[nums[i]] = i