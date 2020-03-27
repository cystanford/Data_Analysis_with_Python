"""
    寻找两个有序数组的中位数
    利用二分查找的优势，求解
"""

# 在nums1[start1,end1], nums2[start2, end2]两个数组中，找第k小的数
def get_kth_num(nums1, start1, end1, nums2, start2, end2, k):
    len1 = end1 - start1 + 1
    len2 = end2 - start2 + 1

    # 让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1 
    if len1 > len2:
        return get_kth_num(nums2, start2, end2, nums1, start1, end1, k)
    if len1 == 0:
        return nums2[start2 + k - 1]

    if k == 1: 
        return min(nums1[start1], nums2[start2])

    # 两个数组，分别前进k/2个数
    i = int(start1 + min(len1, k / 2) - 1)
    j = int(start2 + min(len2, k / 2) - 1)

    if nums1[i] < nums2[j]:
        # 第一个数组，前k/2去掉，在剩余的数组中，继续查找
        return get_kth_num(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
    else:
        # 第二个数组，前k/2去掉，在剩余的数组中，继续查找
        return get_kth_num(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))

# 找两个有序数组中的中位数
def find_median(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    # 第一个中位数
    left = int((n + m + 1) / 2)
    # 第二个中位数
    right = int((n + m + 2) / 2)

    if left == right:
        result = get_kth_num(nums1, 0, n - 1, nums2, 0, m - 1, left)    
    else:
        result = (get_kth_num(nums1, 0, n - 1, nums2, 0, m - 1, left) + get_kth_num(nums1, 0, n - 1, nums2, 0, m - 1, right)) / 2
    return result

"""
nums1 = [1, 2, 3]
nums2 = [4, 5]
"""
nums1 = [1, 3, 5, 7]
nums2 = [1,2,3,4,5,6,7,8,9,10]

print (find_median(nums1, nums2))
    
