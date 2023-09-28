class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        evens = []
        odds = []

        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)

        return (evens + odds)
