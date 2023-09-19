def obtener_suffix_array(cadena):
    sufijos = [
        (cadena[i:], i) for i in range(len(cadena))
    ]  # se crea una lista de todos los sufijos

    sufijos.sort(key=lambda x: x[0])  # se ordena la lista de sufijos

    suffix_array = [
        indice for _, indice in sufijos
    ]  # se crea un array con los indices iniciales de los sufijos ordenados

    return suffix_array


def main():
    cadena = "abracadabra"
    print("Cadena:", cadena)
    print("Suffix Array:", obtener_suffix_array(cadena))


main()
