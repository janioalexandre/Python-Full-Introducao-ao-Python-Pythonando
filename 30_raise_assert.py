def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError("Números negativos não são permitidos")
    return n1 + n2

print(soma(2, 2))
