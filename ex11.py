def acima_da_media(notas):
    return sum(1 for n in notas if n > 5)

print(acima_da_media([3, 6, 7, 2, 8, 4, 5, 9]))