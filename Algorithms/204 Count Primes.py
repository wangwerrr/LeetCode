from math import sqrt
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #  Sieve of Eratosthenes, eleminate all non-prime numbers, the rest are prime numbers. o(n*log(log(n)))
        isPrime = [False] * 2 + [True] * (n-2)
        for i in range(2, int(sqrt(n))+1):
            if not isPrime[i]:
                continue
            for j in range(i**2, n, i):
                isPrime[j] = False
        cnt = 0
        for i in range(2, n):
            if isPrime[i]:
                cnt = cnt + 1
        return cnt
    
    # 0,1,2, ... ,n-1
    # In fact, we can mark off multiples of 5 starting at 5 × 5 = 25, because 5 × 2 = 10 was already marked off by multiple of 2, similarly 5 × 3 = 15 was already marked off by multiple of 3. Therefore, if the current number is p, we can always mark off multiples of p starting at p2, then in increments of p: p2 + p, p2 + 2p, ... 
    
"""
Or we can write like this:

class Solution:
# @param {integer} n
# @return {integer}
def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)



Ver. Time limit exceed
 def countPrimes(self, n):
        def isPrime(k):
            if k == 1:
                return False
            
            for i in range(2, int(sqrt(k)) + 1):
                if k % i == 0:
                    return False
                
            return True
        
        cnt = 0
        for i in range(1, n):
            if isPrime(i):
                cnt = cnt + 1
        
        return cnt
    
"""
   
          
        
