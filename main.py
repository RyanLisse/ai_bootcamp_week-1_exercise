from chefs.surinamese_chef import SurinameseChef
from chefs.italian_chef import ItalianChef
from chefs.jamaica_chef import JamaicaChef

chef_dict = {
    "1": {"class": SurinameseChef, "description": "Surinamese Chef"},
    "2": {"class": ItalianChef, "description": "Italian Chef"},
    "3": {"class": JamaicaChef, "description": "Jamaican Chef"}
}

def get_chef(choice):
    chef_info = chef_dict.get(choice)
    if chef_info:
        return chef_info["class"]()
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