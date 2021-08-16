skaiciai = [1, 2, 3, 5, 6, 7, 8, 9, 10]
lyginiai = []
nelyginiai = []
for skaicius in skaiciai:
    if skaicius == 6:
        break

    if skaicius % 2 == 0:
        lyginiai.append(skaicius)
    else:
        nelyginiai.append(skaicius)

skaiciai = [1, 2, 3, 5, 6, 7, 8, 9, 10]
nauji_skaiciai = []
for i in skaiciai:
    for j in skaiciai:
        if i < j:
            nauji_skaiciai.append(j)

print(nauji_skaiciai)

print(lyginiai)
print(nelyginiai)
