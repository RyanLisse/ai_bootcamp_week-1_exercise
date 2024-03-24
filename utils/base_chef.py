from openai import OpenAI
from .chef_interface import ChefInterface

client = OpenAI()

messages = [{
    "role": "system",
    "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to "
               "cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as "
               "clear as possible and provide the best possible recipes for the user's needs. You know a lot about "
               "different cuisines and cooking techniques. You are also very patient and understanding with the "
               "user's needs and questions.",
}, {
    "role": "system",
    "content": "Your client is going to ask for either a list of ingredients, a dish name, or a recipe. If they "
               "provide a list of ingredients, you should suggest a dish name that can be made with those ingredients. "
               "If they provide a dish name, you should give a detailed recipe for that dish. If they provide a "
               "recipe, you should criticize that recipe and suggest improvements. If the input is not one of these "
               "three options, you should deny the request and ask them to try again.",
}]


class BaseChef(ChefInterface):
    def response(self, input_type, content):
        if input_type == "ingredients":
            ingredients = content
            messages.append(
                {
                    "role": "user",
                    "content": f"Suggest a dish name that can be made with the following ingredients: {ingredients}"
                }
            )
            self._generate_response(messages)

        elif input_type == "dish":
            dish = content
            messages.append(
                {
                    "role": "user",
                    "content": f"Provide a detailed recipe for making {dish}"
                }
            )
            self._generate_response(messages)

        elif input_type == "recipe":
            recipe = content
            messages.append(
                {
                    "role": "user",
                    "content": f"Critique and suggest improvements for the following recipe:\n\n{recipe}"
                }
            )
            self._generate_response(messages)

        else:
            print("Invalid input type. Please provide 'ingredients', 'dish', or 'recipe'.")

    def _generate_response(self, messages):
        model = "gpt-3.5-turbo"

        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )

        while True:
            print("\n")
            user_input = input()
            messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )
            stream = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
            )
            collected_messages = []
            for chunk in stream:
                chunk_message = chunk.choices[0].delta.content or ""
                print(chunk_message, end="")
                collected_messages.append(chunk_message)

            messages.append(
                {
                    "role": "system",
                    "content": "".join(collected_messages)
                }
            )
