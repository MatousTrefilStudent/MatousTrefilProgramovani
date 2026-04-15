import json
import os
import random

SAVE_FILE = "save_game.json"


CROPS = {
    "wheat": {"name": "Psenice", "days": 3, "seed_price": 5, "sell_price": 12, "drought_risk": False, "storm_risk": False},
    "corn": {"name": "Kukurice", "days": 5, "seed_price": 10, "sell_price": 25, "drought_risk": True, "storm_risk": False},
    "tomato": {"name": "Rajce", "days": 4, "seed_price": 15, "sell_price": 40, "drought_risk": True, "storm_risk": True},
    "potato": {"name": "Brambor", "days": 6, "seed_price": 8, "sell_price": 30, "drought_risk": False, "storm_risk": False},
    "sunflower": {"name": "Slunecnice", "days": 7, "seed_price": 20, "sell_price": 65, "drought_risk": True, "storm_risk": True}
}

WEATHER = {
    "sunny": {"name": "Slunecno", "growth": 1, "weight": 0.40},
    "rainy": {"name": "Dest", "growth": 2, "weight": 0.25},
    "cloudy": {"name": "Zatazeno", "growth": 1, "weight": 0.20},
    "drought": {"name": "Sucho", "growth": 0, "weight": 0.10},
    "storm": {"name": "Boure", "growth": 0, "weight": 0.05}
}

PLOT_COST = 50
MAX_PLOTS = 10
STARTING_GOLD = 100
STARTING_PLOTS = 4
WITHER_CHANCE = 0.6


def new_plot():
    """Vytvori a vrati slovnik reprezentujici jednu prazdnou parcelu."""
    return {"crop": None, "days_grown": 0, "ready": False}

def new_game():
    """Vytvori a vrati slovnik reprezentujici novou hru."""
    return {
        "day": 1,
        "gold": STARTING_GOLD,
        "plots": [new_plot() for _ in range(STARTING_PLOTS)],
        "inventory": {},
        "weather_today": "sunny"
    }

# folder path
SAVE_DIR = "Farma_simulator"
SAVE_FILE = os.path.join(SAVE_DIR, "save_game.json")

def save_game(game):
    """Ulozi game slovnik do souboru ve složce Farma_simulator."""
    # Pokud složka neexistuje, vytvoříme ji
    if not os.path.exists("Farma_simulator"):
        os.makedirs(SAVE_DIR)
    
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(game, f, indent=2)

def load_game():
    """Nacte hru ze souboru, nebo vytvori novou hru."""
    # Kontrola existence souboru i cesty
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Chyba při čtení souboru. Zakládám novou hru.")
            return new_game()
    return new_game()



def generate_weather():
    """Nahodne vybere ID pocasi podle vah definovanych v WEATHER."""
    ids = list(WEATHER.keys())
    weights = [WEATHER[w]["weight"] for w in ids]
    return random.choices(ids, weights=weights, k=1)[0]

def advance_day(game):
    """Zpracuje jeden herní den: vygeneruje pocasi, aktualizuje rust plodin."""
    game["weather_today"] = generate_weather()
    current_weather = WEATHER[game["weather_today"]]
    growth = current_weather["growth"]
    weather_id = game["weather_today"]
    
    witherred = []

    for i, plot in enumerate(game["plots"]):
        if plot["crop"] is not None:
            crop_id = plot["crop"]
            crop_data = CROPS[crop_id]
            
            # Kontrola hynutí plodin
            is_drought_risk = weather_id == "drought" and crop_data["drought_risk"]
            is_storm_risk = weather_id == "storm" and crop_data["storm_risk"]
            
            if (is_drought_risk or is_storm_risk) and random.random() < WITHER_CHANCE:
                witherred.append((i + 1, crop_data["name"]))
                plot["crop"] = None
                plot["days_grown"] = 0
                plot["ready"] = False
            else:
                # Přidání růstu, pokud plodina přežila
                if not plot["ready"]:
                    plot["days_grown"] += growth
                    if plot["days_grown"] >= crop_data["days"]:
                        plot["ready"] = True
                        plot["days_grown"] = crop_data["days"]

    game["day"] += 1
    save_game(game)
    return witherred

def harvest(game):
    """Sklidí vsechny parcely oznacene jako ready do inventare."""
    gained = {}
    for plot in game["plots"]:
        if plot["ready"] and plot["crop"] is not None:
            crop_id = plot["crop"]
            
            # Pridani do reportu ze sklizne
            gained[crop_id] = gained.get(crop_id, 0) + 1
            
            # Pridani do inventare hrace
            game["inventory"][crop_id] = game["inventory"].get(crop_id, 0) + 1
            
            # Vynulovani parcely
            plot["crop"] = None
            plot["days_grown"] = 0
            plot["ready"] = False
            
    return gained


def clear():
    """Vycisti terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def print_farm(game):
    """Vycisti terminal a vypise aktualni stav farmy."""
    clear()
    weather_name = WEATHER[game["weather_today"]]["name"]
    
    print(f"DEN: {game['day']:<4} |  ZLATO: {game['gold']:<4} |  POCASI: {weather_name}")
    print("\nPARCELY:")
    
    for i, plot in enumerate(game["plots"]):
        num = f"#{i+1}"
        if plot["crop"] is None:
            print(f"  {num}  [ prazdna   ]")
        elif plot["ready"]:
            crop_name = CROPS[plot['crop']]['name']
            print(f"  {num}  [{crop_name:<10}] *** SKLIDITELNA ***")
        else:
            crop_name = CROPS[plot['crop']]['name']
            grown = plot['days_grown']
            total = CROPS[plot['crop']]['days']
            print(f"  {num}  [{crop_name:<10}] roste {grown}/{total} dni")
            
    print("\nSKLAD:")
    if not game["inventory"]:
        print("  (prazdny)")
    else:
        for crop_id, count in game["inventory"].items():
            crop_name = CROPS[crop_id]["name"]
            print(f"  {crop_name:<10}: {count} ks")
    print("-" * 40)


def plant_crop(game):
    """Zobrazi menu pro vyber prazdne parcely a plodiny, zasadi semeno."""
    empty_plots = [i for i, plot in enumerate(game["plots"]) if plot["crop"] is None]
    
    if not empty_plots:
        print("\nNemáš žádné prázdné parcely!")
        input("Stiskni Enter pro pokracovani...")
        return

    print("\nVyber parcelu k zasazení:")
    for p_idx in empty_plots:
        print(f"  {p_idx + 1}")
    print("  0 pro zrušení")
    
    try:
        plot_choice = int(input("Tvoje volba: "))
    except ValueError:
        print("Neplatný vstup.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    if plot_choice == 0:
        return
    if (plot_choice - 1) not in empty_plots:
        print("Neplatná parcela.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    plot_idx = plot_choice - 1

    print("\nNabídka semen:")
    crop_list = list(CROPS.keys())
    for i, crop_id in enumerate(crop_list):
        c_data = CROPS[crop_id]
        print(f"  {i + 1} - {c_data['name']:<10} (Cena: {c_data['seed_price']} z, Doba: {c_data['days']} dni)")
    print("  0 pro zrušení")
    
    try:
        crop_choice = int(input("Co chceš zasadit: "))
    except ValueError:
        print("Neplatný vstup.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    if crop_choice == 0:
        return
    if crop_choice < 1 or crop_choice > len(crop_list):
        print("Neplatná volba plodiny.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    selected_crop_id = crop_list[crop_choice - 1]
    seed_price = CROPS[selected_crop_id]["seed_price"]
    
    if game["gold"] < seed_price:
        print("\nNemáš dostatek zlata na nákup tohoto semena!")
        input("Stiskni Enter pro pokracovani...")
        return
        
    # Úspěšný nákup a zasazení
    game["gold"] -= seed_price
    game["plots"][plot_idx]["crop"] = selected_crop_id
    game["plots"][plot_idx]["days_grown"] = 0
    game["plots"][plot_idx]["ready"] = False
    
    print(f"\nZasadil jsi {CROPS[selected_crop_id]['name']}.")
    save_game(game)
    input("Stiskni Enter pro pokracovani...")

def do_harvest(game):
    """Sklidí vsechny zrale plodiny a vypise, co bylo sklizeno."""
    gained = harvest(game)
    
    if not gained:
        print("\nNení co sklidit! Žádná parcela není připravená.")
    else:
        print("\nÚspěšně sklizeno:")
        for crop_id, count in gained.items():
            print(f"  {CROPS[crop_id]['name']}: {count}x")
        save_game(game)
        
    input("Stiskni Enter pro pokracovani...")

def sell_crops(game):
    """Zobrazi menu pro prodej plodin ze skladu."""
    if not game["inventory"]:
        print("\nTento sklad je prázdný, nemáš co prodat.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    print("\nCo chceš prodat?")
    inv_list = list(game["inventory"].keys())
    for i, crop_id in enumerate(inv_list):
        count = game["inventory"][crop_id]
        sell_price = CROPS[crop_id]["sell_price"]
        print(f"  {i + 1} - {CROPS[crop_id]['name']:<10} (Máš: {count}x, Výkupní cena: {sell_price} z/ks)")
    print("  0 pro zrušení")
    
    try:
        choice = int(input("Tvoje volba: "))
    except ValueError:
        print("Neplatný vstup.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    if choice == 0:
        return
    if choice < 1 or choice > len(inv_list):
        print("Neplatná volba.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    selected_crop = inv_list[choice - 1]
    max_amount = game["inventory"][selected_crop]
    
    try:
        qty = int(input(f"Kolik kusů chceš prodat (max {max_amount})? "))
    except ValueError:
        print("Neplatný vstup.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    if qty <= 0 or qty > max_amount:
        print("Neplatné množství.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    earned = qty * CROPS[selected_crop]["sell_price"]
    game["gold"] += earned
    game["inventory"][selected_crop] -= qty
    
    if game["inventory"][selected_crop] <= 0:
        del game["inventory"][selected_crop]
        
    print(f"\nProdáno {qty}x {CROPS[selected_crop]['name']} za {earned} zlata.")
    save_game(game)
    input("Stiskni Enter pro pokracovani...")

def buy_plot(game):
    """Prida hracovi novou parcelu za PLOT_COST zlata (max MAX_PLOTS)."""
    if len(game["plots"]) >= MAX_PLOTS:
        print(f"\nUž máš maximální počet parcel ({MAX_PLOTS}).")
        input("Stiskni Enter pro pokracovani...")
        return
        
    if game["gold"] < PLOT_COST:
        print(f"\nNemáš dostatek zlata. Nová parcela stojí {PLOT_COST} z.")
        input("Stiskni Enter pro pokracovani...")
        return
        
    game["gold"] -= PLOT_COST
    game["plots"].append(new_plot())
    print(f"\nÚspěšně jsi zakoupil novou parcelu! Nyní jich máš {len(game['plots'])}.")
    
    save_game(game)
    input("Stiskni Enter pro pokracovani...")

def next_day(game):
    """Posune hru o jeden den dopredu a vypise zpravy o pocasi a skodach."""
    witherred = advance_day(game)
    weather_info = WEATHER[game["weather_today"]]
    
    print(f"\nProbouzíš se do nového dne. Počasí: {weather_info['name']}")
    
    if weather_info["growth"] == 2:
        print("Vydatný déšť urychlil růst tvých plodin!")
    elif weather_info["growth"] == 0:
        print("Extrémní počasí zastavilo růst tvých plodin na tento den.")
        
    if witherred:
        print("\nBOHUŽEL! Následující parcely podlehly nepřízni počasí:")
        for w_plot, w_name in witherred:
            print(f"  Parcela #{w_plot}: {w_name} zahynula.")
            
    input("\nStiskni Enter pro pokracovani...")


def main():
    """Hlavni smycka hry – nacte hru, opakuje: zobraz -> menu -> akce."""
    game = load_game()
    
    while True:
        print_farm(game)
        
        print("AKCE:")
        print("  1 - Zasadit plodinu")
        print("  2 - Sklidit úrodu")
        print("  3 - Prodat ze skladu")
        print("  4 - Koupit parcelu (Cena: ",PLOT_COST," z)")
        print("  5 - Další den")
        print("  6 - Uložit a skončit")
        
        choice = input("\nVyber akci (1-6): ")
        
        if choice == '1':
            plant_crop(game)
        elif choice == '2':
            do_harvest(game)
        elif choice == '3':
            sell_crops(game)
        elif choice == '4':
            buy_plot(game)
        elif choice == '5':
            next_day(game)
        elif choice == '6':
            save_game(game)
            print("\nHra uložena. Měj se farmáři!")
            break
        else:
            print("Neplatná volba. Zadej číslo od 1 do 6.")
            input("Stiskni Enter pro pokracovani...")

if __name__ == "__main__":
    main()