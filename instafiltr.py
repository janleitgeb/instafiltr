from PIL import Image

def uvitani():
    print("vitej v programu pro upravu obrazku!")
    print("========================================")

def nacti_obrazek():
    nazev_souboru = input("zadej nazev souboru s obrazkem (vcetne pripony): ")
    try:
        obrazek = Image.open(nazev_souboru)
        return obrazek
    except FileNotFoundError:
        print("spatnej sosubor, blbecku.")
        return None

def uprav_obrazek(obrazek, choice):
    width, height = obrazek.size
    for x in range(width):
        for y in range(height):
            r, g, b = obrazek.getpixel((x, y))
            if choice == "cernobily":
                diam = int((r + g + b) / 3)
                obrazek.putpixel((x, y), (diam, diam, diam))
            elif choice == "saturated":
                r = min(255, int(r * 1.5))
                g = min(255, int(g * 1.5))
                b = min(255, int(b * 1.5))
                obrazek.putpixel((x, y), (r, g, b))
            elif choice == "bw_lowcon":
                nova_barva = int((r + g + b) / 3)
                if nova_barva < 128:
                    nova_barva -= 30
                else:
                    nova_barva += 50
                nova_barva = max(0, min(255, nova_barva))
                obrazek.putpixel((x, y), (nova_barva, nova_barva, nova_barva))
            elif choice == "bw_highcon":
                nova_barva = int((r + g + b) / 3)
                if nova_barva < 128:
                    nova_barva = 0
                else:
                    nova_barva = 255
                obrazek.putpixel((x, y), (nova_barva, nova_barva, nova_barva))
            elif choice == "inverze":
                obrazek.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    return obrazek

def main():
    while True:
        uvitani()
        obrazek = nacti_obrazek()
        if obrazek:
            volba = input("vyber upravu pro tvoju fotku? ('bw' (cernobily) / saturated / 'bw_lowcon' (cernobily nizky kontrast) / 'bw_highcon' (cernobily vysoky kontrast) / inverze): ")
            upraveny_obrazek = uprav_obrazek(obrazek, volba)
            upraveny_obrazek.show()
            odpoved = input("chces pokracovat (ano/ne)? ").lower()
            if odpoved != "ano":
                break

if __name__ == "__main__":
    main()
