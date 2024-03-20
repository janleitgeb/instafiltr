from PIL import Image

print("vitej na upravvu!")
print("========================================")

nazev_souboru = input("zadej nazev souboru + pripona: ")
try:
    obrazek = Image.open(nazev_souboru)
except FileNotFoundError:
    print("spatne napsany, demente.")
    quit()

volba = input("jak to chces upravit? (cernobily / saturovanejsi): ")

sirka, vyska = obrazek.size
for x in range(sirka):
    for y in range(vyska):
        r, g, b = obrazek.getpixel((x, y))

        # Zvýšení saturace
        r = min(255, int(r * 1.6))  
        g = min(255, int(g * 1.6))  
        b = min(255, int(b * 1.6))  

        # Snížení highlitů
        r = int(r * 0.6)  
        g = int(g * 0.6)  
        b = int(b * 0.6)

        obrazek.putpixel((x, y), (r, g, b))  

obrazek.show()

