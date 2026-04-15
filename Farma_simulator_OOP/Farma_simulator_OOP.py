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

class Plot:
    """One plot on farm"""
    def __init__(self):
        """Creates an empty parcel
        
        Properties:
            Plant:
                name: string identifying type of plant
                days_growth: integer of days of growth this plan had according to weather
                is_ripe: bool identifying if plant is ready for harvest
                """
        self.name=""
        self.days_growth=0
        self.is_ripe=False
    
    def isEmpty(self):
        return self.name == ""

    def plant(self, plantName):
        """adds a plant to the plot"""
        self.name=plantName
        self.days_growth=0
        self.is_ripe=0

        return CROPS[plantName]
    
    def destroy(self):
        self.name=""
        self.days_growth=0
        self.is_ripe=False

    def day(self, weather):
        if ((CROPS[self.plant]["drought_risk"] and weather=="drought") or
            (CROPS[self.plant]["storm_risk"] and weather=="drought")):
            self.destroy()
            return
        self.days_growth+=WEATHER[weather]["growth"]
        self.is_ripe= self.days_growth>=CROPS[self.name]["days"]

        return self.name, self.days_growth, self.is_ripe
    
    def harvest(self):
        if self.is_ripe:
            temp=self.plant
            self.destroy()
            return CROPS[temp]["sell_price"]
        else:
            return "plant can´t be harvested yet"
        
    def getJSON(self):
        return{"name":self.name,"days_growth":self.days_growth,"is_ripe":self.is_ripe}

    @classmethod
    def from_save(cls, data):
        plot =cls()
        plot.name = data["name"]
        plot.days_growth = data["days_growth"]
        plot.is_ripe = data["is_ripe"]
        return plot