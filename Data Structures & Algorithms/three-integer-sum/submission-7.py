class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        output = []

        for i in range(len(sort) - 2):
            if i > 0 and sort[i] == sort[i-1]:
                continue
            
            left = i + 1
            right = len(sort) - 1
            
            while left < right:
                if -sort[i] == sort[left] + sort[right]:
                    output.append([sort[i], sort[left], sort[right]])
                    left += 1
                    right -= 1

                    while left < right and sort[left] == sort[left - 1]:
                        left += 1
                    while left < right and sort[right] == sort[right + 1]:
                        right -= 1

                elif -sort[i] < sort[left] + sort[right]:
                    right -= 1
                else:
                    left += 1
        return output  
