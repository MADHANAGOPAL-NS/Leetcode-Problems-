class Solution:
    def check(self, nums: List[int]) -> bool:
        def sort_nums(nums ,var , index , count):
            if var == nums:
                return True
            elif count >= len(var):
                return False
            else:
                var.append(var[index])
                var.pop(index)
                return sort_nums(nums ,var , index , count+1)
        var = sorted(nums)
        return sort_nums(nums , var , 0 ,0)
