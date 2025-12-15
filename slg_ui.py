#!/usr/bin/env python3
# SLG Strategy Game - Graphical UI Version

import tkinter as tk
from tkinter import ttk, messagebox
import random

class SLGGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SLG Strategy Game")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Initialize game state
        self.game = SLGGame()
        
        # Initialize UI element references
        self.building_labels = {}
        
        # Create UI elements
        self.create_widgets()
        self.update_display()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="🏰 SLG Strategy Game", 
                               font=('Arial', 20, 'bold'), foreground='#e74c3c')
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20))
        
        # Day counter
        self.day_label = ttk.Label(main_frame, text="Day: 1", 
                                  font=('Arial', 14, 'bold'))
        self.day_label.grid(row=1, column=0, columnspan=4, pady=(0, 10))
        
        # Resources frame
        resources_frame = ttk.LabelFrame(main_frame, text="Resources", padding="10")
        resources_frame.grid(row=2, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Resource labels
        self.gold_label = ttk.Label(resources_frame, text="Gold: 100", font=('Arial', 12))
        self.gold_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.food_label = ttk.Label(resources_frame, text="Food: 50", font=('Arial', 12))
        self.food_label.grid(row=0, column=1, padx=10, pady=5)
        
        self.wood_label = ttk.Label(resources_frame, text="Wood: 30", font=('Arial', 12))
        self.wood_label.grid(row=0, column=2, padx=10, pady=5)
        
        self.stone_label = ttk.Label(resources_frame, text="Stone: 20", font=('Arial', 12))
        self.stone_label.grid(row=0, column=3, padx=10, pady=5)
        
        self.population_label = ttk.Label(resources_frame, text="Population: 10/20", font=('Arial', 12))
        self.population_label.grid(row=1, column=0, columnspan=4, pady=5)
        
        # Buildings frame
        buildings_frame = ttk.LabelFrame(main_frame, text="Buildings", padding="10")
        buildings_frame.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Building buttons and labels
        buildings = ['farm', 'lumber_mill', 'mine', 'quarry']
        building_names = {'farm': '🏠 Farm', 'lumber_mill': '🌲 Lumber Mill', 
                         'mine': '⛏️ Mine', 'quarry': '🗿 Quarry'}
        
        self.building_labels = {}
        self.upgrade_buttons = {}
        
        for i, building in enumerate(buildings):
            # Building info label
            label = ttk.Label(buildings_frame, text=f"{building_names[building]}: Level 1", 
                             font=('Arial', 11))
            label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            self.building_labels[building] = label
            
            # Upgrade button
            button = ttk.Button(buildings_frame, text="Upgrade", 
                               command=lambda b=building: self.upgrade_building(b))
            button.grid(row=i, column=1, padx=10, pady=5)
            self.upgrade_buttons[building] = button
        
        # Control buttons frame
        controls_frame = ttk.Frame(main_frame)
        controls_frame.grid(row=4, column=0, columnspan=4, pady=20)
        
        # Next day button
        self.next_day_btn = ttk.Button(controls_frame, text="Next Day", 
                                      command=self.next_day, style='Accent.TButton')
        self.next_day_btn.grid(row=0, column=0, padx=10)
        
        # Status button
        ttk.Button(controls_frame, text="Show Status", 
                  command=self.show_status).grid(row=0, column=1, padx=10)
        
        # Help button
        ttk.Button(controls_frame, text="Help", 
                  command=self.show_help).grid(row=0, column=2, padx=10)
        
        # Event log frame
        self.event_frame = ttk.LabelFrame(main_frame, text="Event Log", padding="10")
        self.event_frame.grid(row=5, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        
        # Event log text area
        self.event_text = tk.Text(self.event_frame, height=8, width=70, font=('Arial', 10))
        self.event_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar for event log
        scrollbar = ttk.Scrollbar(self.event_frame, orient="vertical", command=self.event_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.event_text.configure(yscrollcommand=scrollbar.set)
        
        # Configure grid weights for resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Make event log read-only
        self.event_text.config(state=tk.DISABLED)
    
    def update_display(self):
        """Update all UI elements with current game state"""
        # Update day counter
        self.day_label.config(text=f"Day: {self.game.day}")
        
        # Update resources
        self.gold_label.config(text=f"Gold: {self.game.gold}")
        self.food_label.config(text=f"Food: {self.game.food}")
        self.wood_label.config(text=f"Wood: {self.game.wood}")
        self.stone_label.config(text=f"Stone: {self.game.stone}")
        self.population_label.config(text=f"Population: {self.game.population}/{self.game.max_population}")
        
        # Update building levels
        building_names = {'farm': '🏠 Farm', 'lumber_mill': '🌲 Lumber Mill', 
                         'mine': '⛏️ Mine', 'quarry': '🗿 Quarry'}
        
        for building, info in self.game.buildings.items():
            self.building_labels[building].config(
                text=f"{building_names[building]}: Level {info['level']}"
            )
        
        # Disable next day button if game over
        if self.game.game_over:
            self.next_day_btn.config(state=tk.DISABLED)
    
    def log_event(self, message):
        """Add message to event log"""
        self.event_text.config(state=tk.NORMAL)
        self.event_text.insert(tk.END, f"Day {self.game.day}: {message}\n")
        self.event_text.see(tk.END)  # Auto-scroll to bottom
        self.event_text.config(state=tk.DISABLED)
    
    def upgrade_building(self, building_name):
        """Upgrade a building"""
        if building_name not in self.game.buildings:
            messagebox.showerror("Error", "Invalid building name!")
            return
        
        if self.game.upgrade_building(building_name):
            self.log_event(f"{building_name.title()} upgraded to level {self.game.buildings[building_name]['level']}!")
            self.update_display()
    
    def next_day(self):
        """Advance to next day"""
        if not self.game.game_over:
            self.game.next_day()
            self.update_display()
            
            if self.game.game_over:
                if self.game.population <= 0:
                    messagebox.showerror("Game Over", "Your population has perished!")
                else:
                    messagebox.showinfo("Victory!", "You survived 30 days! Congratulations!")
    
    def show_status(self):
        """Show detailed status in a message box"""
        status_text = f"Day: {self.game.day}\n"
        status_text += f"Resources - Gold: {self.game.gold}, Food: {self.game.food}, Wood: {self.game.wood}, Stone: {self.game.stone}\n"
        status_text += f"Population: {self.game.population}/{self.game.max_population}\n\n"
        status_text += "Buildings:\n"
        
        for building, info in self.game.buildings.items():
            status_text += f"  {building.title()}: Level {info['level']}\n"
        
        messagebox.showinfo("Game Status", status_text)
    
    def show_help(self):
        """Show help information"""
        help_text = """SLG Strategy Game - Help

🎮 Game Objective:
- Survive for 30 days
- Manage your resources wisely
- Keep your population fed

🏗️ Buildings:
- Farm: Produces food
- Lumber Mill: Produces wood  
- Mine: Produces gold
- Quarry: Produces stone

📊 Resources:
- Gold: Used for upgrades
- Food: Required to feed population
- Wood & Stone: Building materials

⚡ Commands:
- Next Day: Advance time
- Upgrade: Improve buildings
- Show Status: View details

💡 Tips:
- Upgrade farms first to ensure food supply
- Balance resource production
- Watch for random events!"""
        
        messagebox.showinfo("Game Help", help_text)

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
    
    def upgrade_building(self, building_name):
        """Upgrade a building if resources are sufficient"""
        if building_name not in self.buildings:
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
            
            return True
        else:
            return False
    
    def collect_resources(self):
        """Collect resources from buildings"""
        self.food += self.buildings['farm']['food_production']
        self.wood += self.buildings['lumber_mill']['wood_production']
        self.gold += self.buildings['mine']['gold_production']
        self.stone += self.buildings['quarry']['stone_production']
    
    def consume_resources(self):
        """Population consumes food"""
        food_needed = self.population
        if self.food >= food_needed:
            self.food -= food_needed
            
            # Chance for population growth if food is sufficient
            if random.random() < 0.3 and self.population < self.max_population:
                self.population += 1
        else:
            # Starvation
            starvation = min(food_needed - self.food, self.population)
            self.population -= starvation
            self.food = 0
    
    def next_day(self):
        """Advance to the next day"""
        self.day += 1
        
        # Collect resources from buildings
        self.collect_resources()
        
        # Population consumes food
        self.consume_resources()
        
        # Random event
        self.random_event()
        
        # Check game over conditions
        if self.population <= 0:
            self.game_over = True
        elif self.day >= 30:
            self.game_over = True
    
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
                break

def main():
    root = tk.Tk()
    app = SLGGameUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()