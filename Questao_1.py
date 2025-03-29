def contar_letra_a(frase):
    # Conta quantas vezes 'a' ou 'A' aparecem na frase
    return frase.lower().count('a')

# Solicita ao usuário uma frase
frase = input("Digite uma frase: ")

# Exibe o resultado
print(f"A letra 'a' aparece {contar_letra_a(frase)} vezes na frase.")