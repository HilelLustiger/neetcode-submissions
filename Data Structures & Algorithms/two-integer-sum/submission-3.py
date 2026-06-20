class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted = {} 
        #{(target - val, index)}
        for i in range(len(nums)):
            wanted[nums[i]] = i
        
        for j in range(len(nums)):
            comp = target - nums[j]
            if target - nums[j] in wanted and j != wanted[comp]:
                return [j, wanted[comp]]
            
