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
        if volba == "cernobily":
            prumer = int((r + g + b) / 3)
            obrazek.putpixel((x, y), (prumer, prumer, prumer))
        elif volba == "saturovanejsi":
            
            r = min(255, int(r * 1.6))  #zvyseni saturace
            g = min(255, int(g * 1.6))  
            b = min(255, int(b * 1.6))  

            r = int(r * 0.7)  #snizeni highlitu
            g = int(g * 0.7)  
            b = int(b * 0.7)  
            obrazek.putpixel((x, y), (r, g, b))

obrazek.show()

