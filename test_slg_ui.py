#!/usr/bin/env python3
# Test script for SLG Game UI

import tkinter as tk
from slg_ui import SLGGameUI

def test_basic_functionality():
    """Test basic functionality of the SLG game UI"""
    print("Testing SLG Game UI...")
    
    # Test importing and creating the game
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the window for testing
        game = SLGGameUI(root)
        print("✓ UI creation successful")
        
        # Test game state initialization
        if hasattr(game, 'game') and hasattr(game.game, 'gold'):
            print(f"✓ Game state initialized - Gold: {game.game.gold}")
        else:
            print("✗ Game state initialization failed")
            return False
            
        # Test resource collection
        initial_food = game.game.food
        game.game.collect_resources()
        if game.game.food > initial_food:
            print(f"✓ Resource collection works - Food increased from {initial_food} to {game.game.food}")
        else:
            print("✗ Resource collection failed")
            return False
            
        # Test building upgrade
        initial_level = game.game.buildings['farm']['level']
        game.game.gold = 1000  # Give enough resources for upgrade
        game.game.wood = 1000
        game.game.stone = 1000
        
        if game.game.upgrade_building('farm'):
            new_level = game.game.buildings['farm']['level']
            if new_level > initial_level:
                print(f"✓ Building upgrade works - Farm level increased from {initial_level} to {new_level}")
            else:
                print("✗ Building upgrade level not increased")
                return False
        else:
            print("✗ Building upgrade failed")
            return False
            
        # Test next day functionality
        initial_day = game.game.day
        game.game.next_day()
        if game.game.day == initial_day + 1:
            print(f"✓ Next day functionality works - Day increased from {initial_day} to {game.game.day}")
        else:
            print("✗ Next day functionality failed")
            return False
            
        print("\n🎉 All tests passed! The SLG Game UI is working correctly.")
        return True
        
    except Exception as e:
        print(f"✗ Error during testing: {e}")
        return False
    finally:
        if 'root' in locals():
            root.destroy()

if __name__ == "__main__":
    test_basic_functionality()