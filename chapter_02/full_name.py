first_name = "ada"
last_name = "lovelace"  # love lace
full_name = first_name + ' ' + last_name
f_string_full_name = f"mano vardas {first_name} {last_name}"

print(full_name)
print(f_string_full_name)

print(full_name.title())

print(full_name.upper())
print(full_name.lower())
print(last_name.isalnum())

print(len(last_name))
print(last_name[0])
print(last_name[1])
print(last_name[0:4])
print(last_name[4:8])
print(last_name[:4])
print(last_name[4:])

pirma_raide = last_name[0]
likusi_dalis = last_name[1:]

pirma_raide, likusi_dalis = last_name[0], last_name[1:]

print(last_name[0].upper() + last_name[1:])
# Uzduotis 3. isspausdinkinte savo varda - pirma raide mazoji, o kitos didziosios.
vardas = "Justas"  # isirasykite savo varda
naujas_vardas = "jUSTAS"

# message = f"Hello, {full_name.title()}!"
# print(message)
