def manacher(cadena):
    s = "#"
    for c in cadena:
        s += c + "#"
    N = len(s)
    P = [0] * N
    C, R = 0, 0
    max_len = 0
    center_index = 0

    for i in range(1, N):
        if R > i:
            mirror = 2 * C - i
            P[i] = min(R - i, P[mirror])

        # Intentar expandir alrededor del centro i
        a = i + 1 + P[i]
        b = i - 1 - P[i]
        while a < N and b >= 0 and s[a] == s[b]:
            P[i] += 1
            a += 1
            b -= 1

        if (
            i + P[i] > R
        ):  # si el palindromo centrado en i sobrepasa R, se reajusta el centro y la expansion
            C = i
            R = i + P[i]

        if P[i] > max_len:
            max_len = P[i]
            center_index = i

    inicio = (center_index - max_len) // 2  # extraemos el palindromo mas largo
    fin = inicio + max_len
    return cadena[inicio:fin]


def main():
    cadena = "babadbabadspaspa"
    palindromo_mas_largo = manacher(cadena)
    print(f"El palindromo mas largo en '{cadena}' es: '{palindromo_mas_largo}'")


main()
