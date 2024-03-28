class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Initialize the result string and the carry
        result = ""
        carry = 0

        # Make sure a is the longer string, swap if it's not
        if len(b) > len(a):
            a, b = b, a

        # Pad the shorter string with zeros on the left
        b = b.zfill(len(a))

        # Iterate over the strings from right to left
        for i in range(len(a) - 1, -1, -1):
            # Calculate the sum of the current digits plus the carry
            current_sum = carry + int(a[i]) + int(b[i])

            # The new digit is the remainder of the current_sum divided by 2
            result = str(current_sum % 2) + result

            # Update the carry (1 if current_sum is 2 or 3, 0 otherwise)
            carry = current_sum // 2

        # If there's a carry left at the end, add it to the result
        if carry:
            result = '1' + result

        return result


a = input("Enter the first binary string: ")
b = input("Enter the second binary string: ")

solution = Solution()

result = solution.addBinary(a, b)

print("The sum of the binary strings is:", result)