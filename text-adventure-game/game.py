def display_message(message):
    print("\n" + message + "\n")

def get_user_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= len(options):
                return choice - 1
            else:
                display_message("Invalid choice. Please choose a valid option.")
        except ValueError:
            display_message("Please enter a number corresponding to your choice.")

def play_game():
    # Game state stored in a dictionary
    game_state = {
        "inventory": [],
        "location": "forest"
    }

    while True:
        if game_state["location"] == "forest":
            display_message("You are in a dark forest. You see paths leading to a cave and a river.")
            choice = get_user_choice(["Go to the cave", "Go to the river", "Quit the game"])
            if choice == 0:
                game_state["location"] = "cave"
            elif choice == 1:
                game_state["location"] = "river"
            elif choice == 2:
                display_message("Thank you for playing!")
                break

        elif game_state["location"] == "cave":
            display_message("You are in a spooky cave. There's a treasure chest here!")
            choice = get_user_choice(["Open the treasure chest", "Go back to the forest", "Quit the game"])
            if choice == 0:
                display_message("You found a magic sword!")
                game_state["inventory"].append("magic sword")
            elif choice == 1:
                game_state["location"] = "forest"
            elif choice == 2:
                display_message("Thank you for playing!")
                break

        elif game_state["location"] == "river":
            display_message("You are at the riverbank. A troll blocks your way.")
            choice = get_user_choice(["Fight the troll", "Go back to the forest", "Quit the game"])
            if choice == 0:
                if "magic sword" in game_state["inventory"]:
                    display_message("You defeated the troll with your magic sword! You win!")
                    break
                else:
                    display_message("You have no weapon to fight the troll. You lose!")
                    break
            elif choice == 1:
                game_state["location"] = "forest"
            elif choice == 2:
                display_message("Thank you for playing!")
                break

if __name__ == "__main__":
    play_game()
