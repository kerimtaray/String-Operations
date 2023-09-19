def calcularZ(cadena, z):
    n = len(cadena)
    l, r = 0, 0  # inicializando las posiciones de la ventana [l, r]
    for i in range(1, n):
        if i > r:
            # si i esta fuera de la ventana [l, r], reinicia l y r
            l, r = i, i
            while (
                r < n and cadena[r - l] == cadena[r]
            ):  # se trata de expandir la ventana [l, r] mientras los caracteres sean iguales
                r += 1
            z[i] = r - l
            r -= 1
        else:  # si i esta dentro de la ventana [l, r], se utilizan los valores anteriores
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while (
                    r < n and cadena[r - l] == cadena[r]
                ):  # se trata de expandir la ventana [l, r] mientras los caracteres sean iguales
                    r += 1
                z[i] = r - l
                r -= 1


def z_algorithm(texto, patron):
    concatenado = patron + "$" + texto
    n = len(concatenado)
    z = [0] * n
    calcularZ(concatenado, z)
    for i in range(n):
        if z[i] == len(patron):
            print(f"PATRON EN INDICE {i - len(patron) - 1}")


def main():
    texto = "KAPADOKALAABABDABACDABABCABAB"
    patron = "ABABCABAB"
    z_algorithm(texto, patron)


main()
