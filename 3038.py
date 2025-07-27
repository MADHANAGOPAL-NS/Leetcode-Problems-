code(python):

Input:
nums = [3,2,1,4,5]

lst = []
curr_sum = 0
for i in range(0 , len(nums) , 2):
    if i+1 < len(nums):
        curr_sum = nums[i] + nums[i+1]
        if len(lst) == 0 or curr_sum == lst[-1]:
            lst.append(curr_sum)
        else:
            break
return len((lst)) 
