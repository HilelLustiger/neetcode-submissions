class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        output = []

        for i in range(len(sort) - 2):
            left = i + 1
            right = len(sort) - 1

            while left < right:
                if sort[left] + sort[right] == -sort[i]:
                    triple = [sort[i], sort[left], sort[right]]
                    if triple not in output:
                        output.append([sort[i], sort[left], sort[right]])
                    right -= 1
                    left += 1
                elif sort[left] + sort[right] > -sort[i]:
                    right -= 1
                else: 
                    left += 1
        
        return output  
