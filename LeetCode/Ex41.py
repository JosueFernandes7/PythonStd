class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
      menorInteiro = 1
      for i in sorted(nums):
        if i == menorInteiro:
           menorInteiro += 1
      return menorInteiro
    

sol = Solution()
lista = [1,2,0]
lista2 = [3,4,-1,1]
lista3 = [7,8,9,11,12]
print(sol.firstMissingPositive(lista) == 3)
print(sol.firstMissingPositive(lista2) == 2)
print(sol.firstMissingPositive(lista3) == 1)