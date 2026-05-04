class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)
        return True if len(nums)!=len(sets) else False