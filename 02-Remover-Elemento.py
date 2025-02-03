# Exercicio 02 - Remover Elemento - Desafio Fase 0 - Python
# Logica a ser seguida:
# Dfinir uma funcao para remover um elemento de uma lista
# Definir a lista com os numeros a serem removidos
# Reconhecer o valor do elemento a ser removido
# Criar uma nova lista sem o elemento a ser removido
# Apresentar o resultado


from typing import List 

class Solution:
    def removeElement(self, nums: List, val: int) -> int:
        k = 0 # Rastreia os elementos validos diferentes de val e armazena a contagem desses elementos
        
        for i in range(len(nums)): # Percorre toda a lista
            if nums[i] != val: # Verifica se o elemento atual eh diferente de val
                nums[k] = nums[i] # Armazena os elementos diferentes de val na propria lista nums
                k += 1
        return k # retorna a contagem de elementos diferentes de val 
    
    # Exemplo 1
nums1 = [3, 2, 2, 3]
val1 = 3
solution = Solution()
k1 = solution.removeElement(nums1, val1)
print(f"Nos restaram {k1} numeroos na lista, a nova lista é {nums1[:k1]}")

# Exemplo 2
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = solution.removeElement(nums2, val2)
print(f"Nos restaram {k2} numeros na lista, a nova lista é {nums2[:k2]}")
    
        