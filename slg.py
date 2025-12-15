#!/usr/bin/env python3
# SLG Strategy Game - Resource Management Simulation

import random
import time

class SLGGame:
    def __init__(self):
        # Game resources
        self.gold = 100
        self.food = 50
        self.wood = 30
        self.stone = 20
        
        # Buildings
        self.buildings = {
            'farm': {'level': 1, 'food_production': 5},
            'lumber_mill': {'level': 1, 'wood_production': 3},
            'mine': {'level': 1, 'gold_production': 2},
            'quarry': {'level': 1, 'stone_production': 2}
        }
        
        # Population
        self.population = 10
        self.max_population = 20
        
        # Game state
        self.day = 1
        self.game_over = False
        
    def display_status(self):
        print(f"\n=== Day {self.day} ===")
        print(f"Resources: Gold: {self.gold} | Food: {self.food} | Wood: {self.wood} | Stone: {self.stone}")
        print(f"Population: {self.population}/{self.max_population}")
        print("Buildings:")
        for building, info in self.buildings.items():
            print(f"  {building.title()}: Level {info['level']}")
    
    def collect_resources(self):
        """Collect resources from buildings"""
        self.food += self.buildings['farm']['food_production']
        self.wood += self.buildings['lumber_mill']['wood_production']
        self.gold += self.buildings['mine']['gold_production']
        self.stone += self.buildings['quarry']['stone_production']
        
        print("\nResources collected for the day!")
    
    def consume_resources(self):
        """Population consumes food"""
        food_needed = self.population
        if self.food >= food_needed:
            self.food -= food_needed
            print(f"Population consumed {food_needed} food")
            
            # Chance for population growth if food is sufficient
            if random.random() < 0.3 and self.population < self.max_population:
                self.population += 1
                print("Population grew by 1!")
        else:
            # Starvation
            starvation = min(food_needed - self.food, self.population)
            self.population -= starvation
            self.food = 0
            print(f"STARVATION! {starvation} people died from hunger!")
    
    def upgrade_building(self, building_name):
        """Upgrade a building if resources are sufficient"""
        if building_name not in self.buildings:
            print("Invalid building name!")
            return False
            
        current_level = self.buildings[building_name]['level']
        cost_multiplier = current_level * 10
        
        costs = {
            'gold': cost_multiplier * 5,
            'wood': cost_multiplier * 3,
            'stone': cost_multiplier * 2
        }
        
        # Check if player has enough resources
        if (self.gold >= costs['gold'] and 
            self.wood >= costs['wood'] and 
            self.stone >= costs['stone']):
            
            # Deduct resources
            self.gold -= costs['gold']
            self.wood -= costs['wood']
            self.stone -= costs['stone']
            
            # Upgrade building
            self.buildings[building_name]['level'] += 1
            
            # Increase production based on building type
            if building_name == 'farm':
                self.buildings[building_name]['food_production'] += 3
            elif building_name == 'lumber_mill':
                self.buildings[building_name]['wood_production'] += 2
            elif building_name == 'mine':
                self.buildings[building_name]['gold_production'] += 2
            elif building_name == 'quarry':
                self.buildings[building_name]['stone_production'] += 1
            
            print(f"{building_name.title()} upgraded to level {self.buildings[building_name]['level']}!")
            return True
        else:
            print("Not enough resources for upgrade!")
            print(f"Cost: Gold: {costs['gold']}, Wood: {costs['wood']}, Stone: {costs['stone']}")
            return False
    
    def random_event(self):
        """Random events that can occur"""
        events = [
            {
                'name': 'Bountiful Harvest',
                'probability': 0.2,
                'effect': lambda: self.food + random.randint(10, 20),
                'message': "A bountiful harvest provides extra food!"
            },
            {
                'name': 'Bandit Raid',
                'probability': 0.15,
                'effect': lambda: self.gold - random.randint(5, 15),
                'message': "Bandits raided your treasury!"
            },
            {
                'name': 'Trade Opportunity',
                'probability': 0.1,
                'effect': lambda: (self.wood + 10, self.gold - 5),
                'message': "A merchant offers a good trade!"
            },
            {
                'name': 'Plague',
                'probability': 0.1,
                'effect': lambda: self.population - random.randint(1, 3),
                'message': "A plague strikes your population!"
            }
        ]
        
        for event in events:
            if random.random() < event['probability']:
                result = event['effect']()
                if isinstance(result, tuple):
                    # Handle multiple resource changes
                    self.wood, self.gold = result
                elif event['name'] == 'Bountiful Harvest':
                    self.food = result
                elif event['name'] == 'Bandit Raid':
                    self.gold = max(0, result)
                elif event['name'] == 'Plague':
                    self.population = max(1, result)
                
                print(f"\n*** EVENT: {event['name']} ***")
                print(event['message'])
                break
    
    def next_day(self):
        """Advance to the next day"""
        self.day += 1
        self.collect_resources()
        self.consume_resources()
        self.random_event()
        
        # Check game over conditions
        if self.population <= 0:
            self.game_over = True
            print("\n💀 GAME OVER - Your population has perished!")
        elif self.day >= 30:
            self.game_over = True
            print("\n🎉 VICTORY! You survived 30 days!")
            self.display_final_score()
    
    def display_final_score(self):
        """Display final game score"""
        score = (self.gold + self.food + self.wood + self.stone) * self.population
        print(f"\n=== FINAL SCORE ===")
        print(f"Days Survived: {self.day}")
        print(f"Final Population: {self.population}")
        print(f"Total Resources: {self.gold + self.food + self.wood + self.stone}")
        print(f"Final Score: {score}")
    
    def show_help(self):
        """Display game instructions"""
        print("\n=== SLG GAME COMMANDS ===")
        print("status - Show current game status")
        print("upgrade [building] - Upgrade a building (farm, lumber_mill, mine, quarry)")
        print("next - Advance to next day")
        print("help - Show this help message")
        print("quit - Exit the game")

def main():
    print("🎮 Welcome to SLG Strategy Game!")
    print("Manage your resources, build your empire, and survive for 30 days!")
    
    game = SLGGame()
    game.show_help()
    
    while not game.game_over:
        try:
            command = input("\nEnter command: ").strip().lower()
            
            if command == 'quit':
                print("Thanks for playing!")
                break
            elif command == 'status':
                game.display_status()
            elif command.startswith('upgrade '):
                building = command.split(' ')[1]
                game.upgrade_building(building)
            elif command == 'next':
                game.next_day()
                if not game.game_over:
                    game.display_status()
            elif command == 'help':
                game.show_help()
            else:
                print("Invalid command. Type 'help' for available commands.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Thanks for playing!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()