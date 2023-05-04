# O desafio do dia 6 foi feito numa plataforma, então não teve código para compartilhar, fiz esse aqui apenas para mostrar um código com funções.
# The challenge on the 6th was done on a platform, so there was no code to share, I made this one just to show a code with functions.
def calcular_média():
    n1 = int(input("Digite a nota 1: "))
    n2 = int(input("Digite a nota 2: "))
    n3 = int(input("Digite a nota 3: "))
    media = ((n1+n2+n3) / 3)
    print(f"A média do aluno é: {media:.2f}")

calcular_média()