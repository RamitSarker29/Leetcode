class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(n):
            product = 1
            while n!=0:
                digit = n%10
                product*=digit
                n //=10
            return product
        while True:
            if digit_product(n) % t ==0:
                return n
            n+=1