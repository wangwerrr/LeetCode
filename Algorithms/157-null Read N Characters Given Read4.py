
class Solution:

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        cnt = 0
        while cnt < n:
            tmp_buf = ""
            num = read4(tmp_buf)
            if num == 0:
                break
            else:
                cnt = cnt + num
                buf = buf + tmp_buf
        
        return cnt
