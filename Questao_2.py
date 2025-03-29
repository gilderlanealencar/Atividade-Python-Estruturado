 
def calcular_idade_futura():
    nome = input("Qual é o seu nome? ")
    idade = int(input("Quantos anos você tem? "))
    ano_atual = 2025
    ano_futuro = 2030
    idade_futura = idade + (ano_futuro - ano_atual)
    
    print(f"Olá, {nome}! Em {ano_futuro}, você terá {idade_futura} anos.")

calcular_idade_futura()