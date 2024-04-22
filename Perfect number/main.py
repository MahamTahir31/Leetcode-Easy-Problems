class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        
        divisor_sum = 1  
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisor_sum += i
                if i != num // i:  
                    divisor_sum += num // i
        return divisor_sum == num

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.checkPerfectNumber(28))  # Output: True
    print(solution.checkPerfectNumber(7))   # Output: False
