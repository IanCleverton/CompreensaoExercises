# Sem compreensões
def achatar(lst):
    resultado = []
    for x in lst:
        if isinstance(x, list):
            resultado += achatar(x)
        else:
            resultado.append(x)
    return resultado

# Com compreensões
def achatar_c(lst):
    return [x for x in lst if not isinstance(x, list)] + \
           [n for x in lst if isinstance(x, list) for n in achatar_c(x)]