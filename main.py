from chefs.surinamese_chef import SurinameseChef
from chefs.italian_chef import ItalianChef
from chefs.jamaica_chef import JamaicaChef
from chefs.brazilian_chef import BrazilianChef
from chefs.dutch_chef import DutchChef

chef_dict = {
    "1": {"class": SurinameseChef, "description": "Surinamese Chef"},
    "2": {"class": ItalianChef, "description": "Italian Chef"},
    "3": {"class": JamaicaChef, "description": "Jamaican Chef"},
   "4": {"class": BrazilianChef, "description": "Brazilian Chef"},
   "5": {"class": DutchChef, "description": "Dutch Chef"}
}

def get_chef(choice):

    chef_info = chef_dict.get(choice)
    if chef_info:
        return chef_info["class"]()
    if choice == "1":
        return SurinameseChef()
    elif choice == "2":
        return ItalianChef()
    elif choice == "3":
        return JamaicaChef()
    elif choice == "4":
        return BrazilianChef()
    elif choice == "5":
        return DutchChef()
    else:
        return None

def main():
    print("👨‍🍳 Welcome to the AI Chef Experience, where flavors meet technology!")
    print("Select your chef:")

    for key, value in chef_dict.items():
        print(f"{key}. {value['description']}")

    while True:
        choice = input("🔢 Enter the number of your choice: ")
        chef = get_chef(choice)
        if chef:
            break

    print("1. 🇸🇷 Surinamese Chef")
    print("2. 🇮🇹 Italian Chef")
    print("3. 🇯🇲 Jamaican Chef")
    print("4. 🇧🇷 Brazilian Chef")
    print("5. 🇳🇱 Dutch Chef")    
    choice = input("🔢 Enter the number of your choice: ")

    chef = get_chef(choice)
    if chef is None:
        print("❌ Invalid choice. Please try again.")

    culinary_adventure_prompt = "\nWhat culinary adventure can I assist you with today?" \
                                "\nA. 🥘 Provide a list of ingredients to suggest a dish." \
                                "\nB. 📖 Provide a recipe for a specific dish." \
                                "\nC. 🍝 Provide a recipe for me to critique."
    print(culinary_adventure_prompt)

    user_choice = input("👉 Enter your choice: ").upper()
    if user_choice in ["A", "B", "C"]:
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