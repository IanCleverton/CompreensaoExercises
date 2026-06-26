def contar_vogais(i):
    return sum(1 for c in i if c in "aeiouAEIOU")
print(contar_vogais("BrasilvaiserHexa"))