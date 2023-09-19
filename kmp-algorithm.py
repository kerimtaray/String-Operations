def calcularLPS(cadena, lps):
    longitud = 0  # longitud del prefijo previo mas largo
    lps[0] = 0  # siempre es cero
    i = 1

    # construimos el array lps[]
    while i < len(cadena):
        if (
            cadena[i] == cadena[longitud]
        ):  # si el character actual coincide con el character del prefijo mas largo
            longitud += 1
            lps[i] = longitud
            i += 1
        else:
            if longitud != 0:  # si no coincide y la longitud no es cero
                longitud = lps[longitud - 1]
            else:  # si la longitud es 0, no hay prefijo que coincida
                lps[i] = 0
                i += 1


def kmp(texto, patron):
    n = len(texto)
    m = len(patron)
    lps = [
        0
    ] * m  # crea el array lps[] que tendra el prefijo mas largo de los sufijos del patron
    calcularLPS(patron, lps)
    i = j = 0
    while i < n:
        if patron[j] == texto[i]:
            i += 1
            j += 1
        if j == m:
            print(f"PATRON EN INDICE: {i - j}")
            j = lps[j - 1]
        elif i < n and patron[j] != texto[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def main():
    texto = "KAPADOKALAABABDABACDABABCABAB"
    patron = "ABABCABAB"
    kmp(texto, patron)


main()
