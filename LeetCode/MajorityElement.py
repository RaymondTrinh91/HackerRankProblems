# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counts = {}
        
#         for n in nums:
#             if counts.get(n):
#                 counts[n] += 1
#             else:
#                 counts[n] = 1
                
#             if counts[n] > len(nums) // 2:
#                 return n


# Second pass with collections
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        majority = len(nums)//2

        for num in count:
            if count[num] > majority:
                return num