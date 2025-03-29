def calcular_estatisticas(numeros):
    if not numeros:
        return "A lista está vazia."
    
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    
    return media, maior, menor

# Exemplo de uso
dados = [10, 20, 30, 40, 50]
media, maior, menor = calcular_estatisticas(dados)
print(f"Média: {media}, Maior: {maior}, Menor: {menor}")
