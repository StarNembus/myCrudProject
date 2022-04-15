"""Учитывая целое число x, вернуть, true если x это целое число палиндрома.

Целое число является палиндромом , если оно читается так же, как в прямом, так и в обратном порядке.

Например, 121есть палиндром, а 123нет."""

"""Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left."""

"""Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome."""


class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[:: -1]


y = Solution()
print(y.isPalindrome(111))
