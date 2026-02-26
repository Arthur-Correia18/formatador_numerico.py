# Projeto: Formatador Numérico em Python
# Autor: Arthur
# Descrição: Demonstra diferentes formas de formatação numérica usando f-strings

print("Olá, seja bem-vindo(a) ao Formatador Numérico!\n")

# Entrada de dados
numero = int(input("Digite um número inteiro: "))

# Exibindo o número em formato decimal
print(f"\nO valor inteiro em decimal é: {numero:d}")

# Exibindo o número em formato binário
print(f"O valor inteiro em binário é: {numero:b}")

# Valor fixo de PI
pi = 3.14159265

print("\nTrabalhando com número decimal (PI):")

# Exibição padrão
print(f"O valor de PI é: {pi:f}")

# Exibição com duas casas decimais
print(f"O valor de PI com duas casas decimais é: {pi:.2f}")