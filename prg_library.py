# -*- coding: utf-8 -*-
"""Společná knihovna pomocných funkcí pro výuku programování v Pythonu.

Modul obsahuje opakovaně používané funkce, které se vyskytují napříč
jednotlivými cvičeními (01-10). Místo opakování kódu stačí importovat:

    from prg_library import clear_terminal, get_float_input, ...

Obsah modulu:
    1.  clear_terminal       — vymazání terminálu (Windows i Linux/Mac)
    2.  get_float_input      — načtení float čísla s validací
    3.  get_int_input        — načtení int čísla s validací
    4.  validate_email       — ověření formátu e-mailové adresy
    5.  print_separator      — tisk oddělovací čáry (volitelně barevně)
    6.  print_header         — tisk nadpisu sekce (volitelně barevně)
    7.  run_menu             — interaktivní textové menu (volitelně barevně)
    8.  ask_continue_or_quit — smyčka „pokračuj nebo ukonči"
    9.  time_consumption     — měření doby výpočtu funkce
    10. log_event            — logování událostí z běhu programu
    11. log_error            — zachycení a zalogování výjimky/chyby
"""

import os
import re
import time
import traceback
from datetime import datetime


# ──────────────────────────────────────────────────────────────────────────────
# Barvy pro terminál — ANSI escape kódy
# ──────────────────────────────────────────────────────────────────────────────
# Na Windows 10+ je potřeba ANSI kódy aktivovat (stačí jednou zavolat os.system("")).
# Na Linuxu a macOS fungují ANSI kódy automaticky.

if os.name == "nt":
    os.system("")                       # aktivace ANSI escape sekvencí na Windows

COLORS = {
    "reset":          "\033[0m",
    "black":          "\033[30m",
    "red":            "\033[31m",
    "green":          "\033[32m",
    "yellow":         "\033[33m",
    "blue":           "\033[34m",
    "magenta":        "\033[35m",
    "cyan":           "\033[36m",
    "white":          "\033[37m",
    "bright_red":     "\033[91m",
    "bright_green":   "\033[92m",
    "bright_yellow":  "\033[93m",
    "bright_blue":    "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan":    "\033[96m",
    "bright_white":   "\033[97m",
    "bold":           "\033[1m",
    "dim":            "\033[2m",
}

# Mapování úrovní logu na barvy v terminálu
_LOG_LEVEL_COLORS = {
    "DEBUG":   "dim",
    "INFO":    "bright_cyan",
    "WARNING": "bright_yellow",
    "ERROR":   "bright_red",
}


def _colorize(text, color=None):
    """Obalí text ANSI escape kódem pro zvolenou barvu.

    Pokud barva není zadána nebo neexistuje ve slovníku COLORS,
    vrátí text beze změny.

    Args:
        text:  řetězec k obarvení
        color: název barvy ze slovníku COLORS (např. "green", "bright_cyan")

    Returns:
        Obarvený (nebo původní) řetězec
    """
    if color and color in COLORS:
        return f"{COLORS[color]}{text}{COLORS['reset']}"
    return text


# ──────────────────────────────────────────────────────────────────────────────
# 1. clear_terminal
# ──────────────────────────────────────────────────────────────────────────────

def clear_terminal():
    """Vymaže obrazovku terminálu.

    Na Windows volá 'cls', na Linuxu a macOS volá 'clear'.

    Příklad:
        >>> clear_terminal()
    """
    os.system("cls" if os.name == "nt" else "clear")


# ──────────────────────────────────────────────────────────────────────────────
# 2. get_float_input
# ──────────────────────────────────────────────────────────────────────────────

def get_float_input(prompt="Zadejte číslo: ",
                    error_msg="Neplatný vstup. Zadejte prosím číslo.",
                    min_value=None):
    """Načte od uživatele desetinné číslo (float) s ošetřením vstupu.

    Opakovaně se ptá, dokud uživatel nezadá platnou hodnotu.
    Volitelně lze nastavit minimální povolenou hodnotu (např. min_value=0
    pro nezáporná čísla, min_value=1 pro kladná čísla).

    Args:
        prompt:    text výzvy zobrazený uživateli
        error_msg: text chybové zprávy při neplatném vstupu
        min_value: minimální povolená hodnota (None = bez omezení)

    Returns:
        Zadané číslo jako float

    Příklady:
        >>> cislo = get_float_input("Zadejte délku strany: ")
        >>> kladne = get_float_input("Kladné číslo: ", min_value=0)
    """
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Hodnota musí být alespoň {min_value}.")
            else:
                return value
        except ValueError:
            print(error_msg)


# ──────────────────────────────────────────────────────────────────────────────
# 3. get_int_input
# ──────────────────────────────────────────────────────────────────────────────

def get_int_input(prompt="Zadejte celé číslo: ",
                  error_msg="Neplatný vstup. Zadejte prosím celé číslo.",
                  min_value=None):
    """Načte od uživatele celé číslo (int) s ošetřením vstupu.

    Opakovaně se ptá, dokud uživatel nezadá platnou celočíselnou hodnotu.
    Volitelně lze nastavit minimální povolenou hodnotu (např. min_value=1
    pro přirozená čísla).

    Args:
        prompt:    text výzvy zobrazený uživateli
        error_msg: text chybové zprávy při neplatném vstupu
        min_value: minimální povolená hodnota (None = bez omezení)

    Returns:
        Zadané číslo jako int

    Příklady:
        >>> n = get_int_input("Kolik čísel? ", min_value=2)
        >>> prirozene = get_int_input("Přirozené číslo: ", min_value=1)
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Hodnota musí být alespoň {min_value}.")
            else:
                return value
        except ValueError:
            print(error_msg)


# ──────────────────────────────────────────────────────────────────────────────
# 4. validate_email
# ──────────────────────────────────────────────────────────────────────────────

def validate_email(email):
    """Zkontroluje, zda e-mail má správný formát.

    Používá regulární výraz pro základní kontrolu: přítomnost znaku @,
    platné znaky před a za @, tečku v doméně a alespoň 2 znaky TLD.

    Args:
        email: e-mailová adresa ke kontrole (str)

    Returns:
        True pokud e-mail má platný formát, jinak False

    Příklady:
        >>> validate_email("student@skola.cz")
        True
        >>> validate_email("spatny-email")
        False
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# ──────────────────────────────────────────────────────────────────────────────
# 5. print_separator
# ──────────────────────────────────────────────────────────────────────────────

def print_separator(char="-", length=50, color=None):
    """Vytiskne oddělovací čáru ze zvoleného znaku.

    Args:
        char:   znak, ze kterého se čára skládá (default "-")
        length: počet opakování znaku (default 50)
        color:  barva textu — název z COLORS, např. "cyan", "yellow" (default None)

    Příklady:
        >>> print_separator()
        --------------------------------------------------
        >>> print_separator("=", 30, "green")
        ==============================          (zeleně)
    """
    line = char * length
    print(_colorize(line, color))


# ──────────────────────────────────────────────────────────────────────────────
# 6. print_header
# ──────────────────────────────────────────────────────────────────────────────

def print_header(title, char="=", length=50, color=None):
    """Vytiskne nadpis sekce orámovaný oddělovači.

    Výstup má tvar:
        ==================================================
           NÁZEV SEKCE
        ==================================================

    Args:
        title:  text nadpisu
        char:   znak pro oddělovač (default "=")
        length: délka oddělovače (default 50)
        color:  barva celého bloku — název z COLORS (default None)

    Příklady:
        >>> print_header("Výsledky")
        >>> print_header("Menu", color="bright_cyan")
    """
    separator = char * length
    block = f"{separator}\n   {title}\n{separator}"
    print(_colorize(block, color))


# ──────────────────────────────────────────────────────────────────────────────
# 7. run_menu
# ──────────────────────────────────────────────────────────────────────────────

def run_menu(options, title="Vyberte akci:", color=None):
    """Zobrazí číslované menu a vrátí volbu uživatele.

    Vypíše nadpis a očíslovaný seznam možností. Opakovaně se ptá,
    dokud uživatel nezadá platné číslo volby.

    Args:
        options: seznam textů jednotlivých voleb, např.
                 ["Registrace", "Přihlášení", "Konec"]
        title:   nadpis menu (default "Vyberte akci:")
        color:   barva nadpisu a čísel voleb (default None)

    Returns:
        Číslo zvolené položky jako int (1 až len(options))

    Příklady:
        >>> volba = run_menu(["Čtverec", "Obdélník", "Kruh"])
        >>> volba = run_menu(["Start", "Konec"], title="Hlavní menu", color="bright_yellow")
    """
    while True:
        print()
        print(_colorize(title, color))
        for i, option in enumerate(options, start=1):
            number = _colorize(f"{i}", color)
            print(f"  {number}. {option}")

        choice = input(f"\nVaše volba (1-{len(options)}): ").strip()

        try:
            choice_int = int(choice)
            if 1 <= choice_int <= len(options):
                return choice_int
        except ValueError:
            pass

        print(_colorize(f"Neplatná volba. Zadejte číslo 1 až {len(options)}.", "red"))


# ──────────────────────────────────────────────────────────────────────────────
# 8. ask_continue_or_quit
# ──────────────────────────────────────────────────────────────────────────────

def ask_continue_or_quit(quit_key="q",
                         prompt=None):
    """Zeptá se uživatele, zda chce pokračovat, nebo ukončit.

    Vrátí True, pokud uživatel stiskne Enter (pokračuje),
    nebo False, pokud zadá quit_key (ukončuje).

    Args:
        quit_key: klávesa pro ukončení, default "q"
        prompt:   text výzvy (default se sestaví automaticky)

    Returns:
        True  — uživatel chce pokračovat (stiskl Enter)
        False — uživatel chce ukončit (zadal quit_key)

    Příklady:
        >>> while ask_continue_or_quit():
        ...     print("Pokračuji...")
        >>> while ask_continue_or_quit("x", "Další kolo? (x = konec): "):
        ...     print("Ještě jednou!")
    """
    if prompt is None:
        prompt = f"Stiskněte Enter pro pokračování nebo '{quit_key}' pro ukončení: "

    answer = input(prompt).strip().lower()
    return answer != quit_key.lower()


# ──────────────────────────────────────────────────────────────────────────────
# 9. time_consumption
# ──────────────────────────────────────────────────────────────────────────────

def time_consumption(func, *args):
    """Změří dobu výpočtu funkce a vrátí čas v milisekundách.

    Volá zadanou funkci s libovolným počtem argumentů a měří
    dobu jejího běhu pomocí time.perf_counter().

    Args:
        func:  funkce, jejíž čas měříme
        *args: argumenty předané měřené funkci

    Returns:
        Doba výpočtu v milisekundách jako float

    Příklady:
        >>> cas = time_consumption(math.factorial, 1000)
        >>> print(f"Výpočet trval {cas:.2f} ms")
        >>> cas = time_consumption(is_prime, 999983)
    """
    start = time.perf_counter()
    func(*args)
    return (time.perf_counter() - start) * 1000


# ──────────────────────────────────────────────────────────────────────────────
# 10. log_event
# ──────────────────────────────────────────────────────────────────────────────

def log_event(message, level="INFO", log_file=None, print_to_terminal=True):
    """Zaloguje událost z běhu programu s časovým razítkem a úrovní.

    Vytvoří záznam ve tvaru:
        [2026-02-12 14:30:25] [INFO   ] Program spuštěn

    Záznam lze vypsat do terminálu (barevně podle úrovně), zapsat do souboru,
    nebo obojí současně.

    Úrovně (level):
        "DEBUG"   — podrobnosti pro ladění (šedý text)
        "INFO"    — běžná informace o průběhu (azurový text)
        "WARNING" — upozornění, program pokračuje (žlutý text)
        "ERROR"   — chyba, ale program nepadá (červený text)

    Args:
        message:           text zprávy (str)
        level:             úroveň záznamu — "DEBUG", "INFO", "WARNING", "ERROR"
                           (default "INFO")
        log_file:          cesta k souboru, do kterého se záznam připojí
                           (default None = nezapisovat do souboru)
        print_to_terminal: zda vypsat záznam do terminálu (default True)

    Returns:
        Zformátovaný řádek logu jako str (pro případné další zpracování)

    Příklady:
        >>> log_event("Program spuštěn")
        [2026-02-12 14:30:25] [INFO   ] Program spuštěn

        >>> log_event("Načteno 42 záznamů", "DEBUG")
        [2026-02-12 14:30:25] [DEBUG  ] Načteno 42 záznamů

        >>> log_event("Soubor nenalezen", "WARNING", log_file="app.log")
        [2026-02-12 14:30:25] [WARNING] Soubor nenalezen
        (+ zápis do app.log)

        >>> log_event("Tiché logování", log_file="app.log", print_to_terminal=False)
        (zápis pouze do souboru, terminál nic nevypíše)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level_upper = level.upper()
    log_line = f"[{timestamp}] [{level_upper:<7}] {message}"

    # Výpis do terminálu — barevně podle úrovně
    if print_to_terminal:
        color = _LOG_LEVEL_COLORS.get(level_upper)
        print(_colorize(log_line, color))

    # Zápis do souboru — čistý text bez ANSI kódů
    if log_file:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")

    return log_line


# ──────────────────────────────────────────────────────────────────────────────
# 11. log_error
# ──────────────────────────────────────────────────────────────────────────────

def log_error(error, context="", log_file=None, print_to_terminal=True):
    """Zachytí a zaloguje výjimku (exception) včetně podrobností.

    Určeno pro použití uvnitř bloku ``except``. Automaticky zjistí typ
    výjimky, její zprávu a traceback (řetězec volání, který k chybě vedl).

    Výstup má tvar:
        [2026-02-12 14:30:25] [ERROR  ] ZeroDivisionError: division by zero
           Kontext: Výpočet podílu dvou čísel
           Soubor "calc.py", řádek 42, ve funkci divide
              return a / b

    Args:
        error:             zachycená výjimka (objekt Exception z except bloku)
        context:           volitelný popis, co program dělal, když chyba nastala
                           (default "" = bez kontextu)
        log_file:          cesta k souboru pro zápis (default None)
        print_to_terminal: zda vypsat do terminálu (default True)

    Returns:
        Celý zformátovaný text chyby jako str

    Příklady:
        Základní použití v except bloku:
        >>> try:
        ...     vysledek = 10 / 0
        ... except Exception as e:
        ...     log_error(e, "Výpočet podílu")

        Pouze zápis do souboru (terminál nic nevypíše):
        >>> try:
        ...     int("abc")
        ... except Exception as e:
        ...     log_error(e, "Převod vstupu", log_file="errors.log",
        ...               print_to_terminal=False)

        Bez kontextu (stačí předat výjimku):
        >>> try:
        ...     data = open("neexistuje.txt")
        ... except Exception as e:
        ...     log_error(e)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_type = type(error).__name__
    error_msg = str(error)

    # Hlavní řádek: typ a zpráva výjimky
    header = f"[{timestamp}] [ERROR  ] {error_type}: {error_msg}"

    # Sestavení podrobností
    details_parts = []

    if context:
        details_parts.append(f"   Kontext: {context}")

    # Traceback — řetězec volání vedoucí k chybě
    tb = traceback.format_exception(type(error), error, error.__traceback__)
    # Vezmeme relevantní řádky tracebacku (vynecháme první a poslední, ty máme)
    tb_lines = "".join(tb).strip().split("\n")
    # Přeskočíme první řádek ("Traceback (most recent call last):") a poslední
    # (ten je duplicitní k naší hlavičce), vybereme prostřední řádky
    if len(tb_lines) > 2:
        relevant_lines = tb_lines[1:-1]        # jen File "...", line ..., + kód
        for line in relevant_lines:
            details_parts.append(f"  {line.strip()}")

    details = "\n".join(details_parts)
    full_output = header + ("\n" + details if details else "")

    # Výpis do terminálu — barevně
    if print_to_terminal:
        print(_colorize(header, "bright_red"))
        if details:
            print(_colorize(details, "red"))

    # Zápis do souboru — čistý text
    if log_file:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(full_output + "\n")

    return full_output


# ──────────────────────────────────────────────────────────────────────────────
# Ukázka použití (spustí se jen při přímém spuštění tohoto souboru)
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    clear_terminal()

    # Ukázka: nadpis a oddělovač s barvou
    print_header("UKÁZKA KNIHOVNY prg_library", color="bright_cyan")
    print()

    # Ukázka: barevné oddělovače
    print_separator("─", 50, "green")
    print("  Zelený oddělovač výše, žlutý níže")
    print_separator("─", 50, "yellow")
    print()

    # Ukázka: validace e-mailu
    print("Validace e-mailu:")
    test_emails = ["student@skola.cz", "spatny-email", "a@b.c", "test@example.com"]
    for email in test_emails:
        result = "OK" if validate_email(email) else "NEPLATNÝ"
        print(f"  {email:25s} → {result}")
    print()

    # Ukázka: menu s barvou
    volba = run_menu(
        ["Načíst float číslo", "Načíst int číslo", "Měření času",
         "Logování a chyby", "Konec"],
        title="Vyberte ukázku:",
        color="bright_yellow"
    )

    if volba == 1:
        cislo = get_float_input("Zadejte desetinné číslo (min 0): ", min_value=0)
        print(f"Zadali jste: {cislo}")

    elif volba == 2:
        cislo = get_int_input("Zadejte celé číslo (min 1): ", min_value=1)
        print(f"Zadali jste: {cislo}")

    elif volba == 3:
        import math
        cas = time_consumption(math.factorial, 5000)
        print(f"Výpočet 5000! trval {cas:.2f} ms")

    elif volba == 4:
        # Ukázka: logování událostí
        print()
        log_event("Program spuštěn")
        log_event("Načítám data ze souboru...", "DEBUG")
        log_event("Soubor config.txt nenalezen, použiji výchozí hodnoty", "WARNING")
        log_event("Uloženo do logu", log_file="ukazka_log.txt", print_to_terminal=False)
        log_event("Všechny záznamy výše + tento jsou v souboru ukazka_log.txt",
                  log_file="ukazka_log.txt")
        print()

        # Ukázka: zachycení chyby
        print_separator("─", 50, "yellow")
        print("Simulace chyb:\n")

        try:
            vysledek = 10 / 0
        except Exception as e:
            log_error(e, "Pokus o dělení nulou", log_file="ukazka_log.txt")

        print()

        try:
            cisla = [1, 2, 3]
            print(cisla[10])
        except Exception as e:
            log_error(e, "Přístup k neexistujícímu prvku seznamu")

        print()

        try:
            int("tohle neni cislo")
        except Exception as e:
            log_error(e)

    elif volba == 5:
        print("Konec ukázky.")

    print()
    print_separator("═", 50, "bright_cyan")
    print(_colorize("  Hotovo!", "green"))
    print_separator("═", 50, "bright_cyan")
