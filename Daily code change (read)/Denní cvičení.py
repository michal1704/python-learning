("28.10. 2026")

cisla = [3, 8, 5, 2, 7]
vybrana = []
soucet = 0

for cislo in cisla:
    if cislo >= 5:
        vybrana.append(cislo)
        soucet += cislo

print(vybrana)
print(soucet)
print()
("29.10.2026")

cisla = [4, 7, 2, 9, 6]
vybrana = []
ostatni = []
soucet = 0

for cislo in cisla:
    if cislo % 2 == 1:
        vybrana.append(cislo)
        soucet += cislo
    else:
        ostatni.append(cislo)

print(vybrana)
print(ostatni)
print(soucet)
