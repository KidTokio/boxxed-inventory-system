import keyboard
import time
from rich.console import Console
import pickle
import os

console = Console()
selection = 0
main_menu = ["View Inventory", "Modify Inventory", "Create Inventory", "Delete Inventory", "Exit"]
modify_menu = ["Add or Modify an Item", "Delete an Item"]

def save_inventories():
    with open('inventories.pkl', 'wb') as file:
        pickle.dump(inventory_list, file)

def load_inventories():
    try:
        with open('inventories.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

inventory_list = load_inventories()

def clear():
    operating_system = os.name

    if operating_system == 'posix':
        os.system('clear')
    elif operating_system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def timer():
    time.sleep(0.15)

def title():
    console.print(f"""[yellow]
.______     ______   ___   ___ ___   ___  _______  _______  
|   _  \   /  __  \  \  \ /  / \  \ /  / |   ____||       \ 
|  |_)  | |  |  |  |  \  V  /   \  V  /  |  |__   |  .--.  |
|   _  <  |  |  |  |   >   <     >   <   |   __|  |  |  |  |
|  |_)  | |  `--'  |  /  .  \   /  .  \  |  |____ |  '--'  |
|______/   \______/  /__/ \__\ /__/ \__\ |_______||_______/   

|-------------------------- V.1.0 -------------------------|
    [/yellow]""")

def quit_program():
    title()
    console.print(f"[yellow]Goodbye! Thanks for using Boxxed[/yellow]", style="bold")
    time.sleep(3)
    exit()

def menu(options, selection):
    title()
    for x, option in enumerate(options):
        if x == selection:
            console.print(f"[yellow]◆ {option}[/yellow]", style="bold")
        else:
            console.print(f"[white]{option}[/white]")
    
    console.print(f"\n[yellow][🡱][/yellow][white] move selection up[/white]    [yellow][🡳][/yellow][white] move selection down[/white]    [yellow][ENTER][/yellow][white] select[/white]")

def navigator():
    global selection
    selection = 0
    
    clear()
    menu(main_menu, selection)
    
    while True:
        key = keyboard.read_key(suppress=True)

        if key == "up":
            selection = (selection - 1) % len(main_menu)
        elif key == "down":
            selection = (selection + 1) % len(main_menu)

        elif key == "enter":
            if selection == 0:
                clear()
                view_inventory()
                break
            elif selection == 1:
                clear()
                modify_inventory()
                break
            elif selection == 2:
                clear()
                create_inventory()
                break
            elif selection == 3:
                clear()
                delete_inventory()
                break
            elif selection == 4:
                clear()
                quit_program()

        timer()
        clear()
        menu(main_menu, selection)

def view_inventory():
    title()
    console.print(f"[yellow]List of saved inventories[/yellow]\n", style="bold")

    if len(inventory_list) == 0:
        console.print(f"[red]You don't have any inventory[/red]")
        time.sleep(2)
        navigator()
    else:
        for inv, _ in inventory_list:
            console.print(f"[white]{inv}[/white]", style="bold")
        console.print(f"\n[yellow]Enter the name of the inventory you want to review or type[/yellow] [red]'cancel'[/red] [yellow]to return to the menu.[/yellow]\n")
        inventory_name = input("")

        if inventory_name == "cancel":
            timer()
            clear()
            navigator()
        else:
            inventory_found = False

            for name, inventory in inventory_list:
                if name == inventory_name:
                    inventory_found = True
                    clear()
                    title()
                    console.print(f"[yellow]Inventory '{inventory_name}'[/yellow]\n", style="bold")
                    for item, quantity in inventory.items():
                        console.print(f"[cyan]{item}[/cyan]: {quantity}")

                    console.print(f"\n[yellow][ESC][/yellow][white] return to menu[/white]")

                    keyboard.wait("esc")
                    timer()
                    navigator()
                    
                if not inventory_found:
                        clear()
                        title()
                        console.print(f"[red]No inventory found with the name '{inventory_name}'[/red]")
                        time.sleep(2)
                        save_inventories()
                        clear()
                        view_inventory()

def modify_inventory():
    title()
    console.print(f"[yellow]List of saved inventories[/yellow]\n", style="bold")

    if len(inventory_list) == 0:
        console.print(f"[red]You don't have any inventory[/red]")
        time.sleep(2)
        navigator()
    else:
        for inv, _ in inventory_list:
            console.print(f"[white]{inv}[/white]", style="bold")

        console.print(f"\n[yellow]Enter the name of the inventory you want to modify or type[/yellow] [red]'cancel'[/red] [yellow]to return to the menu.[/yellow]\n")
        inventory_name = input("")

        if inventory_name == "cancel":
            timer()
            clear()
            navigator()
        
        else:
            inventory_found = False

            for name, inventory in inventory_list:
                if name == inventory_name:
                    inventory_found = True
                    clear()
                    title()
                    console.print(f"[yellow]Inventory '{inventory_name}'[/yellow]\n", style="bold")
                    for item, quantity in inventory.items():
                        console.print(f"[cyan]{item}[/cyan]: {quantity}")
                        
                    console.print(f"\n[yellow][A][/yellow][white] add or modify an item[/white]    [yellow][E][/yellow][white] delete an item[/white]    [yellow][ESC][/yellow][white] return to menu[/white]")

                if not inventory_found:
                    clear()
                    title()
                    console.print(f"[red]No inventory found with the name '{inventory_name}'[/red]")
                    time.sleep(2)
                    navigator()

                while True:
                        key = keyboard.read_key(suppress=True)

                        if key == "a":
                            clear()
                            title()
                            console.print(f"[yellow]Adding/modifying an item in the inventory '{inventory_name}'[/yellow]\n", style="bold")
                            console.print(f"[yellow]Enter the name of the item you want to add/modify or type[/yellow][red] 'cancel'[/red][yellow] to return to the menu[/yellow]\n")
                            item_name = input("")

                            if item_name == "cancel":
                                clear()
                                title()
                                console.print(f"[red]Operation canceled successfully[/red]")
                                time.sleep(2)
                                clear()
                                modify_inventory()
                            elif item_name == "":
                                clear()
                                title()
                                console.print(f"[red]You must enter a valid name[/red]")
                                time.sleep(2)
                                clear()
                                modify_inventory()
                            else:
                                clear()
                                title()
                                console.print(f"[yellow]Adding a new item to the inventory '{inventory_name}'[/yellow]\n", style="bold")
                                console.print(f"[yellow]Enter the quantity of the item you want to add/modify or type[/yellow][red] 'cancel'[/red][yellow] to return to the menu[/yellow]\n")
                                item_quantity = input("")

                                if item_quantity == "cancel":
                                    clear()
                                    title()
                                    console.print(f"[red]Operation canceled successfully[/red]")
                                    time.sleep(2)
                                    clear()
                                    modify_inventory()
                                elif item_quantity == "":
                                    clear()
                                    title()
                                    console.print(f"[red]You must enter a valid quantity[/red]")
                                    time.sleep(2)
                                    clear()
                                    modify_inventory()
                                else:
                                    inventory[item_name] = [item_quantity]
                                    clear()
                                    title()
                                    console.print(f"[yellow]Item added/modified successfully[/yellow]")
                                    time.sleep(2)
                                    clear()
                                    save_inventories()
                                    modify_inventory()
                        
                        if key == "e":
                            clear()
                            title()
                            console.print(f"[yellow]Deleting an item in the inventory '{inventory_name}'[/yellow]\n", style="bold")
                            console.print(f"[yellow]Enter the name of the item you want to delete or type[/yellow][red] 'cancel'[/red][yellow] to return to the menu[/yellow]\n")
                            item_name = input("")

                            if item_name == "cancel":
                                clear()
                                title()
                                console.print(f"[red]Operation canceled successfully[/red]")
                                time.sleep(2)
                                clear()
                                modify_inventory()
                            elif item_name == "":
                                clear()
                                title()
                                console.print(f"[red]Enter a valid name![/red]")
                                time.sleep(2)
                                clear()
                                modify_inventory()
                            else:
                                for name, inventory in inventory_list:
                                    if name == inventory_name:

                                        if item_name in inventory:
                                            del inventory[item_name]
                                            clear()
                                            title()
                                            console.print(f"[yellow]The item '{item_name}' has been deleted from the inventory '{inventory_name}'[/yellow]")
                                            time.sleep(2)
                                            save_inventories()
                                            clear()
                                            modify_inventory()
                                        else:
                                            clear()
                                            title()
                                            console.print(f"[red]The item '{item_name}' does not exist in the inventory '{inventory_name}'![/red]")
                                            time.sleep(2)
                                            clear()
                                            modify_inventory()
                        
                        if key == "esc":
                            modify_inventory()


def create_inventory():
    title()
    console.print(f"[yellow]Creating an inventory[/yellow]", style="bold")
    console.print(f"[yellow]Enter the name of your inventory or type[/yellow] [red]'cancel'[/red] [yellow]to return to the menu.[/yellow]\n")
    timer()
    inventory_name = console.input("")

    if inventory_name == "cancel":
        timer()
        clear()
        navigator()
    else:
        inventory_exists = any(name == inventory_name for name, _ in inventory_list)

        if inventory_exists:
            clear()
            title()
            console.print(f"[red]The inventory '{inventory_name}' already exists.[/red]")
            time.sleep(2)
            navigator()
        else:
            new_inventory = dict()
            inventory_list.append((inventory_name, new_inventory))
            clear()
            title()
            console.print(f"[yellow]Inventory '{inventory_name}' created successfully![/yellow]")
            time.sleep(2)
            save_inventories()
            navigator()

def delete_inventory():
    title()
    console.print(f"[yellow]List of saved inventories[/yellow]\n", style="bold")

    if len(inventory_list) == 0:
        console.print(f"[red]You don't have any inventory[/red]")
        time.sleep(2)
        navigator()
    else:
        for inv, _ in inventory_list:
            console.print(f"[white]{inv}[/white]", style="bold")
        console.print(f"[yellow]\nDeleting an inventory[/yellow]", style="bold")
        console.print(f"[yellow]Enter the name of your inventory or type[/yellow] [red]'cancel'[/red] [yellow]to return to the menu.[/yellow]\n")
        timer()
        inventory_name = console.input("")

        if inventory_name == "cancel":
            timer()
            clear()
            navigator()
        else:

            inventory_found = False

            for i, (name, content) in enumerate(inventory_list):
                if name == inventory_name:
                    inventory_found = True
                    del inventory_list[i]
                    clear()
                    title()
                    console.print(f"[yellow]Inventory '{inventory_name}' deleted successfully![/yellow]")
                    time.sleep(2)
                    save_inventories()
                    clear()
                    navigator()
                    break
            if not inventory_found:
                clear()
                title()
                console.print(f"[red]No inventory found with the name '{inventory_name}'[/red]")
                time.sleep(2)
                clear()
                navigator()

navigator()
