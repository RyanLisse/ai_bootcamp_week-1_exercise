class ChefInterface:
    def response(self, input_type, content):
        raise NotImplementedError("Each chef must implement the response method.")
