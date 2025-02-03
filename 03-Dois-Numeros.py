# Exercicio 03 - Dois Numeros - Desafio Fase 0 - Python
# Logica a ser seguida:
# Definir uma função que percorra umna lista de numeros e encontre dois valores que somados sejam iguais ao alvo
# Definir a lista de numeros e o alvo
# Percorrer a lista de numeros
# Encontrar os dois numeros que somados sejam iguais ao alvo


from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)): # Percorre toda a lista
            for j in range(i + 1, len(nums)): # Percorre toda a lista a partir do proximo indice, para garantir que somemos o mesmo indice duas vezes
                if nums[i] + nums[j] == target: # Verifica se a soma dos dois numeros é igual ao alvo
                    return [i, j]    # Retorna a posicao dos dois numeros
 
        
# Exemplo 1:
nums1 = [2, 7, 11, 15]
target1 = 9
solution = Solution()
saida1 = solution.twoSum(nums1, target1)
print(f"Entrada: {nums1}, alvo: {target1} => Saída: {saida1} => {nums1[saida1[0]]} + {nums1[saida1[1]]} = {nums1[saida1[0]] + nums1[saida1[1]]}") 

#Exemplo 2:
nums2 = [3, 2, 4]
target2 = 6
saida2 = solution.twoSum(nums2, target2)
print(f"Entrada: {nums2}, alvo: {target2} => Saída: {saida2} => {nums2[saida2[0]]} + {nums2[saida2[1]]} = {nums2[saida2[0]] + nums2[saida2[1]]}")

# PS: Após definir a logica e conseguir elaborar um código que funcionasse de acordo, vi que poderia ter utilizado uma função mais eficiente com a ajuda de um dicionario e a função enumerate
# Porem quando  defini a logica primaria com meus conhecimentos até aqui, não conhecia essa outra solução, que me foi apresentada pela i.a. ao pedir uma avaliação do meu codigo. 
# Então optei por deixar essa resolução pois foi a que o meu conhecimento alcançava e fiquei
# satisfeito com o resultado. Mesmo assim busquei enteder a solução eficiente e a compreendi. 