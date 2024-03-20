"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_segunda_columna = 0
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')  # Cambio de ',' a '\t' para dividir las columnas correctamente
            try:
                suma_segunda_columna += int(columns[1])  # Sumar valores de la segunda columna
            except ValueError:
                # Si hay un error al convertir, se continua con la siguiente línea
                continue
    return suma_segunda_columna


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    registro_letras = {}
    with open('data.csv', 'r') as file:
        for line in file:
            letra = line.strip().split('\t')[0]
            registro_letras[letra] = registro_letras.get(letra, 0) + 1
    return sorted(registro_letras.items())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    suma_por_letra = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            valor = int(columns[1])
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
    return sorted(suma_por_letra.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros_por_mes = {}
    with open('data.csv', 'r') as file:
        for line in file:
            mes = line.strip().split('\t')[2].split('-')[1]
            registros_por_mes[mes] = registros_por_mes.get(mes, 0) + 1
    return sorted(registros_por_mes.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    max_min_por_letra = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            valor = int(columns[1])
            if letra not in max_min_por_letra:
                max_min_por_letra[letra] = [valor, valor]
            else:
                max_min_por_letra[letra][0] = max(max_min_por_letra[letra][0], valor)
                max_min_por_letra[letra][1] = min(max_min_por_letra[letra][1], valor)
    return [(letra, max_min[0], max_min[1]) for letra, max_min in sorted(max_min_por_letra.items())]



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    valor_por_clave = {}
    with open('data.csv', 'r') as file:
        for line in file:
            claves_valores = line.strip().split('\t')[4].split(',')
            for par in claves_valores:
                clave, valor = par.split(':')
                valor = int(valor)
                if clave not in valor_por_clave:
                    valor_por_clave[clave] = [valor, valor]
                else:
                    valor_por_clave[clave][0] = min(valor_por_clave[clave][0], valor)
                    valor_por_clave[clave][1] = max(valor_por_clave[clave][1], valor)
    return [(clave, min_max[0], min_max[1]) for clave, min_max in sorted(valor_por_clave.items())]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    valor_por_letra = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            valor = int(columns[1])
            letra = columns[0]
            if valor not in valor_por_letra:
                valor_por_letra[valor] = [letra]
            else:
                valor_por_letra[valor].append(letra)
    return [(valor, letras) for valor, letras in sorted(valor_por_letra.items())]


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    valor_por_letras = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            valor = int(columns[1])
            letra = columns[0]
            if valor not in valor_por_letras:
                valor_por_letras[valor] = {letra}
            else:
                valor_por_letras[valor].add(letra)
    return [(valor, sorted(list(letras))) for valor, letras in sorted(valor_por_letras.items())]


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    claves_contador = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columnas = line.strip().split('\t')[4].split(',')
            for clave_valor in columnas:
                clave, _ = clave_valor.split(':')
                claves_contador[clave] = claves_contador.get(clave, 0) + 1
    return claves_contador


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    resultados = []
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            longitud_col4 = len(columns[3].split(','))
            longitud_col5 = len(columns[4].split(','))
            resultados.append((letra, longitud_col4, longitud_col5))
    return resultados


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra_col4 = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            valor = int(columns[1])
            letras_col4 = columns[3].split(',')
            for letra in letras_col4:
                suma_por_letra_col4[letra] = suma_por_letra_col4.get(letra, 0) + valor
    return {letra: total for letra, total in sorted(suma_por_letra_col4.items())}


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_por_letra_col1 = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letra = columns[0]
            valores_col5 = [int(x.split(':')[1]) for x in columns[4].split(',')]
            suma_por_letra_col1[letra] = suma_por_letra_col1.get(letra, 0) + sum(valores_col5)
    return {letra: total for letra, total in sorted(suma_por_letra_col1.items())}
