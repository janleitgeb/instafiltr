from PIL import Image

def uvitani():
    print("Vítejte v programu pro úpravu obrázků!")
    print("========================================")

def nacti_obrazek():
    nazev_souboru = input("Zadejte název souboru s obrázkem (včetně přípony): ")
    try:
        obrazek = Image.open(nazev_souboru)
        return obrazek
    except FileNotFoundError:
        print("Soubor nenalezen.")
        return None

def uprav_obrazek(obrazek, volba):
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
                obrazek.putpixel((x, y), (r, g, b))
    return obrazek

def main():
    uvitani()
    obrazek = nacti_obrazek()
    if obrazek:
        volba = input("Jak chcete upravit obrázek? (cernobily / saturovanejsi): ")
        upraveny_obrazek = uprav_obrazek(obrazek, volba)
        upraveny_obrazek.show()

if __name__ == "__main__":
    main()