# Exercicio 01 - Numero Romano - Desafio Fase 0 - Python
# Logica a ser seguida:

# 1. Criar uma legenda com os numeros romanos e seus respectivos valores
# 2. Entender a regra de conversao do numero romano para decimal
# 3. Percorrer o numero romano e aplicar as regras de conversao
# 4. Apresentar o resultado

class Solution:
    def romanToInt(self, s):
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} # Dicionario com os numeros romanos
        total = 0 # Armazena o resultado final do numero convertido
        conjunto = []  # Armazena a  explicação final da conversão
        i = 0 

        while i < len(s): # Vai percorrer toda a string           
            if i < len(s) - 1 and romanos[s[i]] < romanos[s[i + 1]]: # Caso especial de subtração, quando o proximo numero romano for maior. Para no penultimo indice da lista.
                valor = romanos[s[i + 1]] - romanos[s[i]] # Calcula a subtração entre o proximo e o atual - Exemplo: IV = 4
                conjunto.append(f"{s[i]}{s[i + 1]} = {valor}")  # Armazena o resultado da subtração no final da lista (append) 
                total += valor
                i += 2  # Avança dois caracteres 
            else:
                # Em caso de repetições, agrupamos (ex: III vira III = 3)
                grupo = s[i]
                valor_grupo = romanos[s[i]]
                while i + 1 < len(s) and s[i] == s[i + 1]:  # Enquanto o proximo caractere for igual ao atual, continue
                    grupo += s[i + 1]
                    valor_grupo += romanos[s[i + 1]]
                    i += 1  # Avança para o próximo
                
                conjunto.append(f"{grupo} = {valor_grupo}")
                total += valor_grupo
                i += 1  # Avança um indice pra evitar processar o mesmo indice mais de uma vez

        explicacao = ", ".join(conjunto)  
        return total, explicacao  

# Criando uma instância da classe Solution
solution = Solution()

# Exemplo 1
entrada1 = "III"    
saida1, explicacao1 = solution.romanToInt(entrada1)
print(f"Entrada: '{entrada1}' => Saída: {saida1}")
print(f"Explicação: {explicacao1}\n")

# Exemplo 2
entrada2 = "LVIII"    
saida2, explicacao2 = solution.romanToInt(entrada2)
print(f"Entrada: '{entrada2}' => Saída: {saida2}")
print(f"Explicação: {explicacao2}\n")

# Exemplo 3
entrada3 = "MCMXCIV"    
saida3, explicacao3 = solution.romanToInt(entrada3)
print(f"Entrada: '{entrada3}' => Saída: {saida3}")
print(f"Explicação: {explicacao3}\n")





    