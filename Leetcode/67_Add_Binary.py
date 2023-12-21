class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
        
    
# Test
obj = Solution()
print(obj.addBinary("11", "1"))
print(obj.addBinary("1010", "1011"))

# a = 0b100
# b = 0b101

## 16lik sanoq sistemasi: 0,1,2,3,4,5,6,7,8,9,A,B,C,E,D,F
# a = 0xF
# b = 0xA
# print(a + b)

## 8lik sanoq sistemasi: 0,1,2,3,4,5,6,7,8
a = 0o11
b = 0o10
print(a + b)
