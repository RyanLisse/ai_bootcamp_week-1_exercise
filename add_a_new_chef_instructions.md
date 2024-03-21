## Adding a New Chef Personality to the AI Chef Experience

To enrich the AI Chef Experience with diverse culinary expertise, you can easily introduce new chef personalities into the application. This guide outlines the steps to add a new chef, from creating the chef's class to integrating it into the main application flow.

### Step 1: Create the Chef's Class
Start by defining a new class for your chef in the `chefs/` directory. For example, to add a French Chef, you would create a file named `french_chef.py`. This class should inherit from `BaseChef` and implement any specific behaviors or attributes.

```python
from utils.base_chef import BaseChef

class FrenchChef(BaseChef):
    def __init__(self):
        super().__init__()
        self.personality = {
            "role": "system",
            "content": "Your description of the French Chef's personality here."
        }
```

### Step 2: Implement Response Logic
Inside your chef class, implement the response logic tailored to the chef's culinary style. This could involve overriding existing methods from `BaseChef` or adding new methods to handle specific types of requests (e.g., ingredients, dish, or recipe).

### Step 3: Integrate the Chef into the Main Application
Modify the `get_chef` function within `main.py` to include an option for selecting your new chef. This involves adding a new condition to return an instance of your chef class based on the user's input.

```python
from chefs.french_chef import FrenchChef

def get_chef(choice):
    if choice == "1":
        return SurinameseChef()
    elif choice == "2":
        return ItalianChef()
    elif choice == "3":  # New option for the French Chef
        return FrenchChef()
    else:
        return None
```

Remember to update the user prompts in `main()` to include the new chef as an option.

### Step 4: Document the New Chef
Update the README.md to include information about the new chef personality, enriching the project's documentation and informing users about the new option available for their culinary adventure.

Following these steps will seamlessly integrate a new chef personality into the AI Chef Experience, broadening the culinary horizons for your users.