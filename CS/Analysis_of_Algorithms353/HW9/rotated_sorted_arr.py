class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target: return m
            elif nums[l] <= nums[m]:
                l, r = (l, m - 1) if nums[l] <= target < nums[m] else (m + 1, r)
            else:
                l, r = (m + 1, r) if nums[m] < target <= nums[r] else (l, m - 1)
        
        return -1
    

solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 1

result = solution.search(nums, target)
print(result)