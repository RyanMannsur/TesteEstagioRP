def eh_fibonacci(n):
    if n <= 1:
        return True

    fib_atual, fib_anterior = 1, 0
    while fib_atual < n:
        aux = fib_atual
        fib_atual = fib_atual + fib_anterior
        fib_anterior = aux

    if fib_atual == n:
        return True
    else:
        return False
    
numero_informado = int(input('Informe um numero inteiro positivo: '))
if numero_informado < 0:
    print('Por favor, informe um numero positivo.')
else:
    if eh_fibonacci(numero_informado):
        print('{} pertence a sequencia de Fibonacci.' .format(numero_informado))
    else:
        print('{} não pertence a sequencia de Fibonacci.' .format(numero_informado))
