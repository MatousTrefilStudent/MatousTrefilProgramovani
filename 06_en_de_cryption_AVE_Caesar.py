import random

# Používaná abeceda (včetně diakritiky a některých symbolů)
alphabet = "aábcčdďefghiíjklmnňopqrřsštťuvwxyz .,!?:-()0123456789"


def caesar_shift(text, shift):
    """
    Jednoduchý Caesar shift.

    Args:
        text (str): Text, který se má posunout.
        shift (int): Posun (kladný i záporný).

    Returns:
        str: Posunutý text.
    """
    output = ""
    for ch in text:
        output += alphabet[(alphabet.index(ch.lower()) + shift) % len(alphabet)]
    return output


def caesar_shift_complicated_en(text, shift):
    """
    Komplikovaná šifrovací funkce.
    Každých 20 znaků:
        - vygeneruje nový náhodný addedShift
        - před text vloží jeho zašifrované dvouciferné vyjádření
    
    Šifrování každého znaku:
        alphabet[(index + shift + addedShift) % len(alphabet)]

    Args:
        text (str): Text k zašifrování.
        shift (int): Základní posun.

    Returns:
        str: Zašifrovaný text včetně vložených klíčů.
    """
    output = ""
    addedShift = 0

    for i, ch in enumerate(text):

        # Každých 20 znaků se vygeneruje nový addedShift
        if i % 20 == 0:
            temp = addedShift
            addedShift = random.randint(0, 100)

            # Přidání dvouciferného klíče zašifrovaného Caesarovým posunem
            output += caesar_shift(f"{addedShift:02d}", (temp + shift))

        # Šifrování znaku
        output += alphabet[(alphabet.index(ch.lower()) + shift + addedShift) % len(alphabet)]

        # Debug výpis (přesunut do main – zde zrušen)

    return output


def caesar_shift_complicated_de(text, shift):
    """
    Dešifrovací funkce k caesar_shift_complicated_en.

    Každých 22 znaků:
        - přečte další dva znaky jako šifrovaný addedShift
        - odstraní tyto dva znaky z výstupu
        - pokračuje v dešifrování

    Args:
        text (str): Zašifrovaný text.
        shift (int): Základní posun použitý při šifrování.

    Returns:
        str: Dešifrovaný text.
    """
    output = ""
    addedShift = 0

    for i, ch in enumerate(text):

        # Každých 22 znaků se zjistí inserted addedShift
        if i % 22 == 0:
            addedShift = int(caesar_shift(text[i:i + 2], -shift - addedShift))

        # Dešifrování znaku
        output += alphabet[(alphabet.index(ch.lower()) - shift - addedShift) % len(alphabet)]

        # Odstranění dvou znaků s klíčem po jejich přečtení
        if i % 22 == 1:
            output = output[:-2]

    return output


def main():
    """Hlavní funkce programu – obsahuje jen výpisy a ukázky."""
    print(caesar_shift("ahooj", 5))
    print(caesar_shift(caesar_shift("ahooj", 5), -5))

    text = "Ahoj jak se máš????  Já se mám dobře jak ty? taky, tráva roste slunce svítí na pasece roste kvítí"

    encrypted = caesar_shift_complicated_en(text, 12)
    print(encrypted)

    decrypted = caesar_shift_complicated_de(encrypted, 12)
    print(decrypted)


if __name__ == "__main__":
    main()
