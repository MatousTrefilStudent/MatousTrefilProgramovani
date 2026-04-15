import json
import os
import random

GOODS = {
    "food":"potraviny",
    "minerals":"mineraly",
    "tech":"technika"
}

PLANETS = {
"terra":{"name":"Terra", "food":10, "minerals":35, "tech":55},
"mars":{"name":"Mars", "food":28, "minerals":12, "tech":48},
"nexus":{"name":"Nexus", "food":45, "minerals":22, "tech":18}
}

"""| ID | Název | Efekt | Pravděpodobnost |
|---|---|---|---|
| `pirates` | Útok pirátů | ztráta 80 kreditů | 0.20 |
| `asteroid` | Asteroidové pole | zisk až 3 ks náhodného zboží zdarma | 0.25 |
| `smooth` | Klidná plavba | zisk 15 kreditů (úspora paliva) | 0.55 |"""

CARGO_CAPACITY   = 20    # maximální počet kusů v nákladu celkem
STARTING_CREDITS = 500   # počáteční kredity hráče
TARGET_CREDITS   = 2000  # počet kreditů potřebný k vítězství
PIRATE_LOSS      = 80    # kredity ztracené při přepadení

EVENTS ={
"pirates":{"name":"Útok pirátů", f"effect":"ztráta {PIRATE_LOSS} kreditů", "probability":0.20},
"asteroid":{"name":"Asteroidové pole", "effect":"zisk až 3 ks náhodného zboží zdarma", "probability":0.25},
"smooth":{"name":"Klidná plavba", "effect":"zisk 15 kreditů (úspora paliva)", "probability":0.55}
}

def new_game():
    return {"day":1, 
          "credits":STARTING_CREDITS, 
          "cargo":{"food": 0, "minerals": 0, "tech": 0}, 
          "location":"terra", 
          }
    
def save_game(game):
    if not os.path.exists("Vesmirny_obchodnik"):
        os.makedirs(os.path.join("Vesmirny_obchodnik", "save_game.json"))
    
    with open(os.path.join("Vesmirny_obchodnik", "save_game.json"), "w", encoding="utf-8") as f:
        json.dump(game, f, indent=2)

def load_game():
    if os.path.exists(os.path.join("Vesmirny_obchodnik", "save_game.json")):
        try:
            with open(os.path.join("Vesmirny_obchodnik", "save_game.json"), "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Chyba při čtení souboru. Zakládám novou hru.")
            return new_game()
    return new_game()


def print_status(game):
    print("="*50)
    print(f"  DEN: {game['day']}   |   KREDITY: {game['credits']}   |   CIL: {TARGET_CREDITS}")
    print(f"  PLANETA: {PLANETS[game['location']]['name']}")
    print("="*50)
    print("\nNAKLAD ({} / {} j.):".format(sum(game["cargo"].values()), CARGO_CAPACITY))
    for good, amount in game["cargo"].items():
        print(f"  {GOODS[good].capitalize():<15}: {amount} ks")
    
    print("\nCENY NA {}:".format(PLANETS[game['location']]['name'].upper()))
    for good, price in PLANETS[game["location"]].items():
        if good in GOODS:
            print(f"  {GOODS[good].capitalize():<15}: {price} kr/ks")

def main():
    game = load_game()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print_status(game)
        print("""\nAkce:\n\t1. Koupit zboží\n\t2. Prodat zboží\n\t3. Cestovat\n\t4. Uložit a skončit""")

        choice = input("Zvolte akci (1-4):\t")

        os.system("cls" if os.name == "nt" else "clear")
        print_status(game)

        if "1" in choice:
            print("\nCo chcete koupit?")
            for i, good in enumerate(GOODS.keys(), 1):
                print(f"\t{i}. {GOODS[good].capitalize()} ({PLANETS[game['location']][good]} kr/ks)")
            
            good_choice = input("Zvolte zboží (1-3):\t")
            if good_choice in ["1", "2", "3"]:
                good_key = list(GOODS.keys())[int(good_choice)-1]
                price = PLANETS[game["location"]][good_key]
                max_affordable = game["credits"] // price
                max_space = CARGO_CAPACITY - sum(game["cargo"].values())
                max_buyable = min(max_affordable, max_space)
                
                if max_buyable <= 0:
                    print("Nemáte dostatek kreditů nebo místa v nákladu.")
                    continue
                
                quantity = input(f"Kolik ks {GOODS[good_key].capitalize()} chcete koupit? (max {max_buyable}):\t")

                if quantity.isdigit() and 0 < int(quantity) <= max_buyable:
                    quantity = int(quantity)
                    game["cargo"][good_key] += quantity
                    game["credits"] -= quantity * price
                    print(f"Koupili jste {quantity} ks {GOODS[good_key].capitalize()}.")
                else:
                    print("Neplatný počet.")
            else:
                print("Neplatná volba zboží.")

        if "2" in choice:
            print("\nCo chcete prodat?")
            for i, good in enumerate(GOODS.keys(), 1):
                print(f"\t{i}. {GOODS[good].capitalize()} ({PLANETS[game['location']][good]} kr/ks)")
            good_choice = input("Zvolte zboží (1-3):\t")
            if good_choice in ["1", "2", "3"]:
                good_key = list(GOODS.keys())[int(good_choice)-1]
                price = PLANETS[game["location"]][good_key]
                max_sellable = game["cargo"][good_key]
                
                if max_sellable <= 0:
                    print("Nemáte žádné zboží k prodeji.")
                    continue
                
                quantity = input(f"Kolik ks {GOODS[good_key].capitalize()} chcete prodat? (max {max_sellable}):\t")
                if quantity.isdigit() and 0 < int(quantity) <= max_sellable:
                    quantity = int(quantity)
                    game["cargo"][good_key] -= quantity
                    game["credits"] += quantity * price
                    print(f"Prodali jste {quantity} ks {GOODS[good_key].capitalize()}.")
                else:
                    print("Neplatný počet.")
            else:
                print("Neplatná volba zboží.")

        if "3" in choice:
            print("\nKam chcete cestovat?")

            for i, planet in enumerate(PLANETS.keys(), 1):
                print(f"\t{i}. {PLANETS[planet]['name']}")
            planet_choice = input("Zvolte planetu (1-3):\t")

            if planet_choice in ["1", "2", "3"]:
                new_location = list(PLANETS.keys())[int(planet_choice)-1]
                game["location"] = new_location
                game["day"] += 1
                
                event_roll = random.random()
                cumulative_prob = 0.0
                for event_key, event in EVENTS.items():
                    cumulative_prob += event["probability"]
                    if event_roll < cumulative_prob:
                        print(f"\nNáhodná událost: {event['name']} - {event['effect']}")
                        if event_key == "pirates":
                            game["credits"] = max(0, game["credits"] - PIRATE_LOSS)
                        elif event_key == "asteroid":
                            free_goods = random.randint(1, 3)
                            good_key = random.choice(list(GOODS.keys()))
                            available_space = CARGO_CAPACITY - sum(game["cargo"].values())
                            actual_free = min(free_goods, available_space)
                            game["cargo"][good_key] += actual_free
                            print(f"Získali jste {actual_free} ks {GOODS[good_key].capitalize()} zdarma.")
                        elif event_key == "smooth":
                            game["credits"] += 15
                        break
            else:
                print("Neplatná volba planety.")

        if "4" in choice:
            save_game(game)
            print("Hra uložena. Nashledanou!")
            break

        if game["credits"] >= TARGET_CREDITS:
            print("\nGratulujeme! Dosáhli jste cíle a stali se nejúspěšnějším vesmírným obchodníkem!")
            save_game(game)
            break
    
if __name__ == "__main__":
    main()
