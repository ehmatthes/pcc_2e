def funkcijos_vardas(argumentas_1, argumentas_2):
    suma = argumentas_1 + argumentas_2
    if suma < 8:
        return "maziau nei astuoni"
    return suma


rezultatas = funkcijos_vardas(argumentas_1=1, argumentas_2=11)

print(rezultatas)

rezultatas = funkcijos_vardas(argumentas_1=1, argumentas_2=2)

print(rezultatas)

