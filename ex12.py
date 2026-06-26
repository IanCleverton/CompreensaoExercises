def letras(palavras):
    return [c for p in palavras for c in p]

print(letras(["Brasil", "Hexa"]))