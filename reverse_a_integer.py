class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            n = x*(-1)
        else:
            n = x
        m = str(n)
        sample = []
        rev = 0
        for i in m:
            sample.append(i)
            
        for i in range(len(sample)-1,-1,-1):
            j = int(sample[i])
            rev = rev+ j *  pow(10,i)
        if rev < (-2 ** 31) or rev > (2**31 -1):
            return 0
        elif x < 0:
            return rev*(-1)
        else:
            return rev
            