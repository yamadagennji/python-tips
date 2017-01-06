class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        bb=[]
        from itertools import combinations
        for k in range(0,len(nums)+1):
            aa=combinations(nums, k)
            bb.extend(aa)
        bb=list(set(bb))
        return(bb)
