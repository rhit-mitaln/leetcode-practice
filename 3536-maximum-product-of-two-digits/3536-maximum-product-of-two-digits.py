class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """

        digits = [int(d) for d in str(n)]

        if (n >= 10 and n <=99):
            return digits[0]*digits[1]

        fmax = 0 # fmax refers to the maximum digit
        smax = 0 # smax refers to second maximum digit 

        for dig in digits:
            if (dig == fmax):
                smax = fmax
            if (dig > fmax):
                smax = fmax
                fmax = dig
            if (dig < fmax and dig > smax):
                smax = dig
            

        return smax * fmax


