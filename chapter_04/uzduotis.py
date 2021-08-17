# Parašyti funkciją, kuriai perduodami du kintamieji a ir b.
# Kintamasis a yra sveikųjų skaičių sąrašas, kintamasis b yra sveikasis skaičius.
# Kintamajame a raskite pirmą dviejų skaičių porą, kurios suma yra lygi kintamajam b.
# Jeigu tokios poros nėra, praneškite.
#
# Pirmas atvejis
a = [1, 2, 3, 4, 4, 5, 6, 7]
b = 13


#
# Antras atvejis
# a = [1,6,10,2], b = 12

def pora(a, b):
    for num in a:
        a.remove(num)
        skirtumas = b - num
        if skirtumas in a:
            return f"Pora rasta : {num} + {skirtumas} = {b}"
    return f"Pora nerasta"

print(pora(a = [2,1,6,6,10,2], b = 12))