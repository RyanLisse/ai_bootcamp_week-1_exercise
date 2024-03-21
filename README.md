
# 👨‍🍳 AI Chef Experience 🍝

This project is a fun and interactive command-line application that allows users to interact with different AI chefs, each with its own unique personality and culinary expertise. Users can provide ingredients, dish names, or recipes, and the AI chefs will respond accordingly, suggesting dishes, providing recipes, or critiquing the provided recipe.

## Features

- Multiple AI chef personalities to choose from
- Suggest dish names based on provided ingredients
- Provide detailed recipes for given dish names
- Critique and suggest improvements for provided recipes

## Installation

Before installing project dependencies, it's recommended to set up a Python virtual environment. This helps to keep dependencies required by different projects separate by creating isolated environments for them. Follow these steps to set up your virtual environment and install the required packages.

1. **Set Up Virtual Environment**:

   If you don't have a virtual environment yet, create one by running:

   ```bash
   python -m venv env
   ```

   Activate the virtual environment:

    - On Unix/macOS, run:

      ```bash
      source env/bin/activate
      ```

    - On Windows, run:

      ```bash
      env\Scripts\activate.bat
      ```

2. **Install Dependencies**:

   With the virtual environment activated, install the project dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

   This command installs all the necessary packages as specified in the `requirements.txt` file, ensuring that you have the right versions needed for the project.

## Usage

1. Run the `main.py` script.
2. Select the desired AI chef personality.
3. Choose the input type: "ingredients", "dish", or "recipe".
4. Follow the prompts and interact with the AI chef.

## Example
👨‍🍳 Welcome to the AI Chef Experience, where flavors meet technology!
Select your chef:

🇸🇷 Surinamese Chef
🇮🇹 Italian Chef 🔢 Enter the number of your choice: 2
What culinary adventure can I assist you with today?
A. 🥘 Provide a list of ingredients to suggest a dish.
B. 📖 Provide a recipe for a specific dish.
C. 🍝 Provide a recipe for me to critique.
👉 Enter your choice: B

🍽️ Enter the name of the dish: Carbonara
