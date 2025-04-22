
def get_prompt(dish: str) -> str:    # Generates a formatted prompt based on dish name
    return (
        f"Give me a recipe for {dish}. Limit the steps to a maximum of 10. "
        "Only return cooking instructions, numbered step-by-step, in clear format. "
        "Respond in JSON with a 'steps' key."
    )

