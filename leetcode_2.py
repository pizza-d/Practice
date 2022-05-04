### Two Sum

### solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L_len = len(nums)
        for i in range(L_len):
            for j in range(i+1,L_len):
                if nums[i] + nums[j] == target:
                    return [i,j]
                  
### solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for key,val in enumerate(nums):
            val2 = target - val
            try:
                key2 = nums[key+1:].index(val2)
            except:
                key2 = -1
            if key2 > -1:
                return [key,key2+key+1]
            
### solution 3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for key,val in enumerate(nums):
            val2 = target - val
            if val2 in check:
                return [check[val2],key]
            check[val] = key
