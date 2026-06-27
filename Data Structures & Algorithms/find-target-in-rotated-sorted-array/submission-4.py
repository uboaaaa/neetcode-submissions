class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        min_ind = float('inf')

        # find pivot point's index
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                min_ind = mid
                break
            
        # set l and r depending on target's location relative to max and min val of array
        if min_ind == 0:
            l, r = 0, len(nums) - 1
        elif target <= nums[-1]:
            l, r = mid, len(nums) - 1
        else:
            l,r = 0, mid
        
        # run regular binary search after setting l and r
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
        

            
