# 2021-08-16
# 1.  hello_world.py - kaip paleisti skripta ir terminale isspausdinti pasisveikinima.
print("Hello world!")
# Uzduotis 1. prasyk skripta, kuris isspausdintu tavo Varda ir Pavarde.

# 2. Komentaru rasymas.
# as esu komentaras
print("Hello world! 2")  # as esu dar vienas komentaras
# Uzduotis 2. isspausdinikite eilute, kurioje butu panaudotos kabutes.

# 3. Strings (Eilutes) ir kintamieji
# Kaireje puseje yra kintamojo vardas, desineje puseje yra kintamojo reiksme
# pirma yra ivykdoma desine puse.

first_name = "John"
last_name = "Paul"
full_name = first_name + ' ' + last_name  # naudojant pliusa galima sujungti dvi eilutes
f_string_full_name = f"My name is {first_name} {last_name}"  # f-string leidzia eilutese naudoti kintamuosius
print(full_name)
print(f_string_full_name)

# 4. Eiliuciu slice'inimas. Eilute galima isivaizduoti kai raidziu list'a (sarasa).
print(first_name[0])  # isspausdins kintamojo first_name pirma raide
print(last_name[1:3])  # isspaudins kintamojo last_name antra ir trecia raides.
# indeksas prasideda nuo 0, indekso intervalas yra [start:end), start pakliuna i rezultata, end nepakliuna i rezultata.
# Uzduotis 3. isspausdinkinte savo varda - pirma raide mazoji, o kitos didziosios.

# 5. Eilutes turi ivairius metodus. Pvz.
message = f"Hello, {full_name.title()}!"
print(message)
message = f"Hello, {full_name.upper()}!"
print(message)

# 6. List - Sarasas
# Sarasas yra elementu rinkinys.
bicycles = ['trek', 'trek', 'cannondale', 'redline', 'specialized']
bicycles.append('MTB')  # ideti nauja elementa saraso gale
bicycles.insert(2, 'new_MTB')  # ideti nauja elementa saraso indekso 2 vietoje.
bicycles.remove('trek')  # pasalinti pirma elementa lygu 'trek'
dviratis = bicycles.pop(0)  # paimti pirma elementa ir ji pasalinti is saraso
# Sarasa galima slaisinti kaip ir eilutes.

# 7. Saraso rikiavimas
a = [1, 2, 3, 5, 4]
a.sort()
print(a)
b = ['456', '123', '781']
b.sort(reverse=True)
print(b)
b.sort(key=lambda x: x[-1])
print(b)


def antras_elemtas(x):
    return x[1]


vardai_pavardes = [['Justin', 'Bieber'], ['Jonas', 'Jonaitis'], ['Zilvinas', 'Adomaitis']]
vardai_pavardes.sort(key=antras_elemtas)
print(vardai_pavardes)

# Uzduotis 4. parasyti cikla, kuris sarase paliktu tik unikalius elementus. input ['a', 'a', 'b', 'c', 'c'], output ['a', 'b', 'c']

# 8. Salygos
a = 8
if a < 8:
    print(f'{a} maziau uz astuonis')
elif a == 8:
    print(f'{a} yra lygu astuoniems')
else:
    print(f'{a} yra daugiau uz astuonis')

a = 8
b = 9
print(a == b)
print(a <= b)
print(a >= b)
print(a != b)
print(a < b)
print(a > b)

# 9. Ciklas

skaiciai = [1, 2, 3, 5, 6, 7, 8, 9, 10]
lyginiai = []
nelyginiai = []
for skaicius in skaiciai:  # pereinam visus saraso elementus. Iteracijos elemento vardas yra skaicius
    if skaicius % 2 == 0:  # jeigu skaicius dalinasi is 2 ir liekana == 0, tada jis lyginis
        lyginiai.append(skaicius)  # isidedam i lyginiai list'a
    else:
        nelyginiai.append(skaicius)  # jeigu padalinus is 2 liekana nelygi 0 isidedam i nelyginiai lista

print(lyginiai)
print(nelyginiai)


# 10 Funkcijos
def funkcijos_vardas(argumentas_1, argumentas_2):
    suma = argumentas_1 + argumentas_2
    if suma < 8:
        return "maziau nei astuoni"
    return suma


rezultatas = funkcijos_vardas(argumentas_1=1, argumentas_2=11)

print(rezultatas)

rezultatas = funkcijos_vardas(argumentas_1=1, argumentas_2=2)

print(rezultatas)


# Uzduotis 5.
# Parašyti funkciją, kuriai perduodami du kintamieji a ir b.
# # Kintamasis a yra sveikųjų skaičių sąrašas, kintamasis b yra sveikasis skaičius.
# # Kintamajame a raskite pirmą dviejų skaičių porą, kurios suma yra lygi kintamajam b.
# # Jeigu tokios poros nėra, praneškite.
# #
# # Pirmas atvejis
# a = [1, 2, 3, 4, 4, 5, 6, 7]
# b = 13
#
#
# #
# # Antras atvejis
# # a = [1,6,10,2], b = 12
#

def pora(sarasas, skaicius):
    for num in sarasas:
        sarasas.remove(num)
        skirtumas = skaicius - num
        if skirtumas in sarasas:
            return f"Pora rasta : {num} + {skirtumas} = {skaicius}"
    return f"Pora nerasta"


print(pora(sarasas=[2, 1, 6, 6, 10, 2], skaicius=12))
