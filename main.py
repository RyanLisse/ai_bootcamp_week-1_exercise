from chefs.surinamese_chef import SurinameseChef
from chefs.italian_chef import ItalianChef


def get_chef(choice):
    if choice == "1":
        return SurinameseChef()
    elif choice == "2":
        return ItalianChef()
    else:
        return None


def main():
    print("👨‍🍳 Welcome to the AI Chef Experience, where flavors meet technology!")
    print("Select your chef:")
    print("1. 🇸🇷 Surinamese Chef")
    print("2. 🇮🇹 Italian Chef")
    choice = input("🔢 Enter the number of your choice: ")

    chef = get_chef(choice)
    if chef is None:
        print("❌ Invalid choice. Please try again.")
        return

    print("\nWhat culinary adventure can I assist you with today?")
    print("A. 🥘 Provide a list of ingredients to suggest a dish.")
    print("B. 📖 Provide a recipe for a specific dish.")
    print("C. 🍝 Provide a recipe for me to critique.")
    user_choice = input("👉 Enter your choice: ").upper()

    if user_choice == "A":
        ingredients = input("🍅 Enter a list of ingredients (separated by commas): ")
        chef.response("ingredients", ingredients)
    elif user_choice == "B":
        dish_name = input("🍽️ Enter the name of the dish: ")
        chef.response("dish", dish_name)
    elif user_choice == "C":
        recipe = input("🍝 Enter the recipe: ")
        chef.response("recipe", recipe)
    else:
        print("❌ Invalid input. Let's try this again, shall we?")


if __name__ == "__main__":
    main()