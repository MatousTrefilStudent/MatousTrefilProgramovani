import os
import random
import time
from abc import ABC, abstractmethod


##############################################################
def power_boost(func):
    """Dekorátor, který zvýší sílu útoku.
    Dekorátor přidá pevnou hodnotu 10 k základnímu poškození vrácenému původní funkcí.
    Také vytiskne zprávu, že síla útoku byla zvýšena. Využití u válečníka.
    Args:
        func: Původní funkce, která vrací základní poškození.
    Returns:
        wrapper: Nová funkce, která vrací zvýšené poškození a vypíše info.
    """
    def wrapper(*args, **kwargs):
        """Upravená funkce s přidaným efektem. Načte základní poškození a přidá 10 bodů."""
        base_damage = func(*args, **kwargs)
        boosted_damage = base_damage + 10
        print("Síla útoku byla zvýšena o 10 bodů!")
        return boosted_damage
    return wrapper


##############################################################
class PlayableCharacter(ABC):
    """Abstraktní třída definující základní rozhraní pro všechny hratelné postavy."""

    @abstractmethod
    def attack(self):
        """Abstraktní metoda útoku – musí být implementována v potomcích."""
        pass

    @abstractmethod
    def defend(self, damage: int):
        """Abstraktní metoda obrany – musí být implementována v potomcích."""
        pass

    @abstractmethod
    def level_up(self):
        """Abstraktní metoda zvýšení úrovně – musí být implementována v potomcích."""
        pass


##############################################################
class Character(PlayableCharacter):
    """Základní třída pro všechny herní postavy.
    Args:
        name (str): Jméno postavy.
        health (int): Zdraví postavy.
        mana (int): Mana postavy.
        level (int): Úroveň postavy.
    Methods:
        defend: Obrana postavy proti útoku.
        level_up: Zvýšení úrovně postavy.
    Attributes:
        __str__: Textová reprezentace postavy - dunder.
        __add__: Kombinace inventářů dvou postav - dunder.
    """
    MAX_HEALTH = 200

    def __init__(self, name: str, health: int, mana: int, level: int):
        self.name = name
        self._health = min(health, self.MAX_HEALTH)
        self.__mana = mana
        self.level = level
        self.inventory = []

    @property
    def health(self):
        """Getter pro zdraví postavy."""
        return self._health

    @health.setter
    def health(self, value):
        """Nastavení zdraví s kontrolou nula až max."""
        if value > self.MAX_HEALTH:
            self._health = self.MAX_HEALTH
        elif value < 0:
            self._health = 0  # Zdraví nesmí být záporné
        else:
            self._health = value

    @property
    def mana(self):
        """Getter pro manu postavy."""
        return self.__mana

    @mana.setter
    def mana(self, value):
        """Nastavení many s kontrolou nezáporné hodnoty."""
        self.__mana = max(0, value)

    def _use_mana(self, amount: int):
        """Protected metoda: Použití many. Určeno pro interní použití nebo potomky."""
        if self.__mana >= amount:
            self.__mana -= amount
            return True
        return False

    def attack(self):
        """Základní útok postavy. Poškození = náhodné číslo 1–10 × úroveň."""
        return random.randint(1, 10) * self.level

    def defend(self, damage: int):
        """Obrana postavy. Přijmutí poškození sníženého o úroveň postavy."""
        actual_damage = max(0, damage - self.level)
        self.health -= actual_damage

    def level_up(self):
        """Zvýšení úrovně postavy."""
        self.level += 1
        print(f"{self.name} postoupil na úroveň {self.level}!")

    def __str__(self):
        inventar = self.inventory if self.inventory else "prázdný"
        return f"{self.name} (Úroveň: {self.level}, Zdraví: {self.health}, Mana: {self.mana}, Inventář: {inventar})"

    def __add__(self, other):
        """Kombinace inventářů dvou postav (dunder pro sčítání)."""
        if isinstance(other, Character):
            combined_inventory = self.inventory + other.inventory
            return combined_inventory
        raise ValueError("Lze kombinovat pouze inventáře postav.")


##############################################################
class Warrior(Character):
    """Válečník je podtřída třídy Character, která představuje válečníka ve hře,
    specializovaného na fyzické útoky.
    Attributes:
        name (str): Jméno válečníka.
        health (int): Zdraví válečníka.
        mana (int): Mana válečníka.
        level (int): Úroveň válečníka, která ovlivňuje jeho sílu.
        strength (int): Fyzická síla válečníka, vypočítaná jako level * 5.
    Methods:
        __init__(name: str, health: int, mana: int, level: int):
            Inicializuje nového válečníka se zadaným jménem, zdravím, manou a úrovní.
        attack():
            Provádí silný fyzický útok. Způsobené poškození je součtem základního
            poškození útoku z třídy Character a síly válečníka.
    """
    def __init__(self, name: str, health: int, mana: int, level: int):
        super().__init__(name, health, mana, level)
        self.strength = level * 5

    @power_boost
    def attack(self):
        """Fyzický útok válečníka se silou a základním poškozením."""
        return super().attack() + self.strength

    def level_up(self):
        """Zvýšení úrovně válečníka – přidá bonus k síle."""
        super().level_up()
        self.strength += 5
        print(f"Síla {self.name} vzrostla na {self.strength}.")


##############################################################
class Mage(Character):
    """Třída Mage reprezentuje kouzelníka, který je specializovaný na magické útoky.
    Attributes:
        name (str): Jméno kouzelníka.
        health (int): Zdraví kouzelníka.
        mana (int): Mana kouzelníka, potřebná pro kouzlení.
        level (int): Úroveň kouzelníka, která ovlivňuje jeho schopnosti.
        intelligence (int): Inteligence kouzelníka, závislá na jeho úrovni.
    Methods:
        cast_spell():
            Seslání kouzla, které spotřebuje manu a způsobí náhodné
            poškození v závislosti na úrovni kouzelníka.
    """
    def __init__(self, name: str, health: int, mana: int, level: int):
        super().__init__(name, health, mana, level)
        self.intelligence = level * 3

    def attack(self):
        """Základní útok kouzelníka (bez many)."""
        return super().attack()

    def cast_spell(self):
        """Seslání kouzla – spotřebuje 10 many, způsobí poškození dle úrovně a náhody."""
        if self._use_mana(10):
            damage = random.randint(1, 6) * self.level + self.intelligence
            print(f"{self.name} seslal kouzlo!")
            return damage
        print(f"{self.name} nemá dostatek many!")
        return 0

    def level_up(self):
        """Zvýšení úrovně kouzelníka – přidá bonus k inteligenci."""
        super().level_up()
        self.intelligence += 3
        print(f"Inteligence {self.name} vzrostla na {self.intelligence}.")


##############################################################
class Monster:
    """Třída reprezentující příšeru."""
    def __init__(self, name: str, health: int, strength: int):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        """Útok příšery – náhodné poškození v rozsahu síly příšery."""
        return random.randint(1, self.strength)

    def defend(self, damage: int):
        """Příšera přijímá poškození."""
        self.health = max(0, self.health - damage)

    def __str__(self):
        return f"Příšera {self.name} (Zdraví: {self.health}, Síla: {self.strength})"


##############################################################
def generate_random_monster() -> Monster:
    """Vytvoří náhodnou příšeru."""
    names = ["Goblin", "Troll", "Ork", "Drak", "Vlkodlak", "Skelet"]
    name = random.choice(names)
    health = random.randint(40, 100)
    strength = random.randint(10, 25)
    return Monster(name, health, strength)


##############################################################
def generate_random_character() -> Character:
    """Vygeneruje náhodnou herní postavu."""
    warrior_names = ["Thor", "Conan", "Aragorn", "Guts", "Beowulf"]
    mage_names = ["Merlin", "Gandalf", "Saruman", "Yen", "Radagast"]

    char_type = random.choice([Warrior, Mage])
    if char_type == Warrior:
        name = random.choice(warrior_names)
        health = random.randint(120, 180)
        mana = random.randint(10, 30)
    else:
        name = random.choice(mage_names)
        health = random.randint(80, 120)
        mana = random.randint(40, 70)

    level = random.randint(2, 6)
    return char_type(name, health, mana, level)


##############################################################
def generate_random_characters(num: int) -> list:
    """Vygeneruje seznam náhodných herních postav.
    Args:
        num (int): Počet postav k vygenerování.
    Returns:
        list: Seznam postav.
    """
    return [generate_random_character() for _ in range(num)]


##############################################################
def display_characters_status(characters: list):
    """Zobrazí aktuální stav všech postav.
    Args:
        characters (list): Seznam postav.
    """
    print("\n=== Aktuální stav postav ===")
    for character in characters:
        print(character)


##############################################################
def random_event(characters: list):
    """Provede náhodné události mezi koly.
    Args:
        characters (list): Seznam postav.
    """
    items = ["Magic Scroll", "Ohnivý meč", "Lektvar síly", "Starodávný amulet", "Zlatá přilba"]
    events = ["heal", "item", "damage"]

    print("\n=== Náhodné události ===")
    for character in characters:
        event = random.choice(events)
        if event == "heal":
            amount = random.randint(10, 30)
            character.health += amount
            print(f"{character.name} se uzdravil o {amount} zdraví.")
        elif event == "item":
            item = random.choice(items)
            character.inventory.append(item)
            print(f"{character.name} získal nový předmět: {item}.")
        elif event == "damage":
            amount = random.randint(5, 20)
            character.health -= amount
            print(f"{character.name} ztrácí {amount} zdraví.")


##############################################################
def monster_encounter(character: Character):
    """Simuluje setkání postavy s příšerou."""
    monster = generate_random_monster()
    print(f"\n{character.name} narazil na {monster}!")
    time.sleep(1)

    while monster.health > 0 and character.health > 0:
        # Postava útočí
        if isinstance(character, Mage) and character.mana >= 10:
            damage = character.cast_spell()
        else:
            damage = character.attack()
        monster.defend(damage)
        print(f"{character.name} útočí a způsobuje {damage} poškození.")
        print(f"{monster.name} má nyní {monster.health} zdraví.")
        time.sleep(0.5)

        if monster.health <= 0:
            print(f"{monster.name} byl poražen!")
            reward = random.randint(20, 40)
            character.health += reward
            print(f"{character.name} získává {reward} zdraví jako odměnu.")
            break

        # Příšera útočí
        monster_damage = monster.attack()
        character.defend(monster_damage)
        print(f"{monster.name} útočí a způsobuje {monster_damage} poškození.")
        print(f"{character.name} má nyní {character.health} zdraví.")
        time.sleep(0.5)


##############################################################
def battle_round(character1: Character, character2: Character):
    """Simuluje jedno kolo boje mezi dvěma postavami.
    Returns:
        Character | None: Vítěz, nebo None pokud boj pokračuje.
    """
    print("\n--- Kolo boje ---")

    # character1 útočí
    if isinstance(character1, Mage) and character1.mana >= 10:
        damage = character1.cast_spell()
    else:
        damage = character1.attack()
    character2.defend(damage)
    print(f"{character1.name} útočí a způsobuje {damage} poškození.")
    print(f"{character2.name} má nyní {character2.health} zdraví.")
    time.sleep(0.5)

    if character2.health <= 0:
        print(f"{character2.name} byl poražen!")
        return character1

    # character2 útočí
    if isinstance(character2, Mage) and character2.mana >= 10:
        damage = character2.cast_spell()
    else:
        damage = character2.attack()
    character1.defend(damage)
    print(f"{character2.name} útočí a způsobuje {damage} poškození.")
    print(f"{character1.name} má nyní {character1.health} zdraví.")
    time.sleep(0.5)

    if character1.health <= 0:
        print(f"{character1.name} byl poražen!")
        return character2

    return None


##############################################################
def game_loop():
    """Hlavní herní smyčka."""
    print("=== Začíná hra ===\n")
    time.sleep(1)

    characters = generate_random_characters(random.randint(3, 5))

    print("Vygenerované postavy:")
    for character in characters:
        print(character)

    while len(characters) > 1:
        print("\n=== Nové kolo ===")

        # 30% šance na setkání s příšerou
        if random.random() < 0.3:
            chosen = random.choice(characters)
            monster_encounter(chosen)
            if chosen.health <= 0:
                print(f"{chosen.name} byl zabit příšerou a vypadl ze hry!")
                characters.remove(chosen)
                if len(characters) <= 1:
                    break
            time.sleep(1)

        # Náhodně vybereme dva různé soupeře
        fighter1, fighter2 = random.sample(characters, 2)
        print(f"{fighter1.name} a {fighter2.name} se utkají v boji!")
        time.sleep(1)

        winner = None
        while not winner:
            winner = battle_round(fighter1, fighter2)

        loser = fighter2 if winner == fighter1 else fighter1
        characters.remove(loser)

        display_characters_status(characters)

        if len(characters) > 1:
            random_event(characters)

        time.sleep(1)

    if characters:
        print(f"\n=== Hra skončila! Vítězem je {characters[0].name} ===")


##############################################################
if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')

    # STEP 01 – Základní ukázka
    hero1 = Warrior("Pat", 100, 20, 5)
    hero2 = Mage("Mat", 80, 50, 4)

    print(hero1)
    print(hero2)
    print("-"*40)

    # Útok a obrana
    damage = hero1.attack()
    print(f"{hero1.name} útočí a způsobuje {damage} poškození.")
    hero2.defend(damage)
    print(f"Po útoku má {hero2.name} {hero2.health} zdraví.")
    print("-"*40)

    # Kombinace inventářů
    hero1.inventory.append("Meč")
    hero1.inventory.append("Kožená vesta")
    hero2.inventory.append("Hůl")
    print(f"Inventář {hero1.name}: {hero1.inventory}")
    print(f"Inventář {hero2.name}: {hero2.inventory}")
    print("-"*40)

    combined_inventory = hero1 + hero2
    print(f"Kombinovaný inventář: {combined_inventory}")

    print("-"*40)
    print(f"Inventář {hero1.name}: {hero1.inventory}")
    print(f"Inventář {hero2.name}: {hero2.inventory}")
    print("-"*40)
    hero1.inventory = hero1 + hero2
    print(f"Do inventáře {hero1.name} byl přidán inventář {hero2.name}.")
    print(f"Inventář {hero1.name}: {hero1.inventory}")
    print(f"Inventář {hero2.name}: {hero2.inventory}")
    print("-"*40)

    input("\nStiskni Enter pro spuštění simulace hry...\n")
    os.system('clear' if os.name == 'posix' else 'cls')

    # STEP 04–06 – Simulace hry
    game_loop()