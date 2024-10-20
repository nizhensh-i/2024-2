def find_mount(nums: list):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if l == r:
            return r
        elif nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
            return m
        elif nums[m] < nums[m + 1]:
            l = m + 1
        elif nums[m - 1] > nums[m]:
            r = m - 1


# nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
relative_max = find_mount(nums)
print(relative_max)
