class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num >= 10):
            temp = 0
            while(num > 0):
                temp += num % 10
                num /= 10
            num = temp
        return num
"""
Digital Root
this method depends on the truth:
N=(a[0] * 1 + a[1] * 10 + ...a[n] * 10 ^n),and a[0]...a[n] are all between [0,9]
we set M = a[0] + a[1] + ..a[n]
and another truth is that:
1 % 9 = 1
10 % 9 = 1
100 % 9 = 1
so N % 9 = a[0] + a[1] + ..a[n]
means N % 9 = M
so N = M (% 9)
as 9 % 9 = 0,so we can make (n - 1) % 9 + 1 to help us solve the problem when n is 9.as N is 9, ( 9 - 1) % 9 + 1 = 9

class Solution(object):
def addDigits(self, num):
    
    if num == 0 : return 0
    else:return (num - 1) % 9 + 1
"""
