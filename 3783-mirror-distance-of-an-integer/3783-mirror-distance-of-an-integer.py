class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 10:
            return 0
        
        reverse = n 
        revString = ""

        while (reverse > 0):
            reverse, remainder = divmod(reverse, 10)
            revString  = revString + str(remainder)
            print("Reverse: ", reverse, "remainder: ", remainder, "RevString: ", revString)



        return abs(n - int(revString))
        