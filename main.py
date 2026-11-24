import math


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def ler_numeros():
    texto = input("Digite os numeros separados por espaco: ")
    try:
        return [float(x) for x in texto.split()]
    except ValueError:
        print("Entrada invalida. Use apenas numeros.")
        return []


def estatisticas():
    numeros = ler_numeros()
    if not numeros:
        print("Nenhum numero valido informado.")
        return

    ordenados = sorted(numeros)
    n = len(ordenados)
    media = sum(ordenados) / n

    meio = n // 2
    if n % 2 == 0:
        mediana = (ordenados[meio - 1] + ordenados[meio]) / 2
    else:
        mediana = ordenados[meio]

    variancia = sum((x - media) ** 2 for x in ordenados) / n
    desvio = math.sqrt(variancia)

    print(f"Quantidade: {n}")
    print(f"Menor valor: {ordenados[0]}")
    print(f"Maior valor: {ordenados[-1]}")
    print(f"Soma: {sum(ordenados)}")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desvio padrao: {desvio:.2f}")


def verificar_primo():
    try:
        n = int(input("Digite um numero inteiro: "))
    except ValueError:
        print("Entrada invalida. Digite um numero inteiro.")
        return

    if eh_primo(n):
        print(f"{n} e primo.")
    else:
        print(f"{n} nao e primo.")


def listar_primos():
    try:
        limite = int(input("Listar primos ate qual numero? "))
    except ValueError:
        print("Entrada invalida. Digite um numero inteiro.")
        return

    primos = [n for n in range(2, limite + 1) if eh_primo(n)]
    if primos:
        print("Primos:", " ".join(str(p) for p in primos))
    else:
        print("Nao ha primos nesse intervalo.")


def inverter_texto():
    texto = input("Digite um texto: ")
    print("Invertido:", texto[::-1])
    limpo = "".join(c.lower() for c in texto if c.isalnum())
    if limpo and limpo == limpo[::-1]:
        print("Esse texto e um palindromo!")


def menu():
    opcoes = {
        "1": ("Estatisticas de uma lista de numeros", estatisticas),
        "2": ("Verificar se um numero e primo", verificar_primo),
        "3": ("Listar numeros primos ate um limite", listar_primos),
        "4": ("Inverter um texto", inverter_texto),
    }

    while True:
        print("\n=== MINI FERRAMENTAS ===")
        for chave, (descricao, _) in opcoes.items():
            print(f"{chave} - {descricao}")
        print("0 - Sair")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Ate logo!")
            break
        elif escolha in opcoes:
            print()
            opcoes[escolha][1]()
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu()
