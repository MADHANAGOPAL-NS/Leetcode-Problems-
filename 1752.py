class Solution:
    def check(self, nums: List[int]) -> bool:
        def sort_nums(nums ,var1 , index , count):
            if var1 == nums:
                return True
            elif count >= len(var1):
                return False
            else:
                var1.append(var1[index])
                var1.pop(index)
                return sort_nums(nums ,var1 , index , count+1)
        var1 = sorted(nums)
        return sort_nums(nums , var1 , 0 , 0)
