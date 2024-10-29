# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

texto = str(input('Digite sua string aqui: '))
text = texto.lower()
letra = "a"

qtd = text.count(letra)
print(f"A letra {letra} aparece {qtd} vezes na string.")