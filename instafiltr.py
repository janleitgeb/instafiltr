from PIL import Image

print("vitej v programu pro upravu obrazku!")
print("========================================")

nazev_souboru = input("zadej nazev souboru s obrazkem (+ pripona): ")
try:
    obrazek = Image.open(nazev_souboru)
except FileNotFoundError:
    print("neexistuje pico.")
    quit()

volba = input("jak chcete upravit obrazek? (cernobily / saturovanejsi): ")

sirka, vyska = obrazek.size
for x in range(sirka):
    for y in range(vyska):
        r, g, b = obrazek.getpixel((x, y))
        if volba == "cernobily":
            prumer = int((r + g + b) / 3)
            obrazek.putpixel((x, y), (prumer, prumer, prumer))
        elif volba == "saturovanejsi":
            r = min(255, int(r * 1.5))
            g = min(255, int(g * 1.5))
            b = min(255, int(b * 1.5))
            r = int(r * 0.8)
            g = int(g * 0.8)
            b = int(b * 0.8)
            obrazek.putpixel((x, y), (r, g, b))

obrazek.show()
