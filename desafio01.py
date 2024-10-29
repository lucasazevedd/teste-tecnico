# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):

    # A sequência de fibonacci não tem números menores que zero
    if n < 0:
        return "O número não pode ser menor que zero."
    
    # Os primeiros dois valores da sequência de fibonacci
    a = 0
    b = 1

    # Se o número for algum 0 ou 1 automaticamente ele já pertence a sequência de fibonacci
    if n == a or n == b:
        return 'este número pertence a sequência de fibonacci.'
    
    # Cálculo que soma os dois valores anteriores para dar sequência a fibonacci até o número inserido
    while b < n:
        a, b = b, a + b

    # Verifica se o número é o último número calculado na sequência
    if b == n:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."
    

num = int(input('Digite um número maior ou igual a zero: '))
resultado = fibonacci(num)
print(resultado)
