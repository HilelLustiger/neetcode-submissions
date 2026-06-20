class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted = {} 
        #{(target - val, index)}
        for i in range(len(nums)):
            wanted[nums[i]] = i
        
        for j in range(len(nums)):
            if target - nums[j] in wanted and j != wanted[target - nums[j]]:
                return [j, wanted[target - nums[j]]]
            
