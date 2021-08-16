a = [1, 2, 3, 5, 4]
a.sort()

print(sorted(a))

b = ['456', '123', '781']
b.sort(reverse=True)
b.sort(key=lambda x: x[-1])
print(b)

def antras_elemtas(x):
    return x[1]

vardai_pavardes = [['Justas', 'Kalpokas'], ['Jonas', 'Jonaitis'], ['Zilvinas', 'Adomaitis']]
vardai_pavardes.sort(key=antras_elemtas)
print(vardai_pavardes)


def funkcijos_vardas(kintamasis_1, kitamasis_2):
    return kintamasis_1 + kitamasis_2


a = funkcijos_vardas(a, b)
print(a)
print(a)

# a = lambda x, y: x+y
# print(a(1,2))

print(len(a))