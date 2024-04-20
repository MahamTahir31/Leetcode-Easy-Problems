class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = int(num1) + int(num2)
        return str(res)
        

solution = Solution()

n1 = input("Enter number 1: ")
n2 = input("Enter number 2: ")
res = solution.addStrings(n1, n2)
print(res)