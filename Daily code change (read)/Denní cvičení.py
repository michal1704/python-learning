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

