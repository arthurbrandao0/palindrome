def is_palindrome(n):
    """
    Função que verifica se um número é palíndromo.
    """
    return str(n) == str(n)[::-1]


def soma_com_inverso_palindromo(numero):
    """
    Função que verifica se a soma de um número com seu inverso resulta em um número palíndromo.
    Retorna o número de iterações necessárias para alcançar o palíndromo.
    """
    num_iteracoes = 0
    while True:
        inverso = int(str(numero)[::-1])  # Inverte o número
        print(numero)
        soma = numero + inverso

        if is_palindrome(soma):
            return soma, num_iteracoes + 1
        else:
            numero = soma
            num_iteracoes += 1
            print(num_iteracoes)


# Exemplo de uso:
numero = 69
resultado, num_iteracoes = soma_com_inverso_palindromo(numero)
print(f"A soma de {numero} com seu inverso resulta em um número palíndromo após {num_iteracoes} iterações: {resultado}")
