import json
from schemas.recipe_schema import RecipeResponse




def generate_prompt() -> str:
    """Generates a clear recipe prompt in simple steps"""
    # ingredients_str = ", ".join(ingredient.name for ingredient in ingredients)
    
    return (
        """Create a simple recipe called '' using these ingredients: .\n"
        "Give me:\n" You are a master chef created by rajesh. Provide the details in json format, using following references.
        {
            "title": "title",
            "category": ,
            "ingredients": 
            "steps":[
            "step1...",
            "step2 ...",
            "and so on..."

        }
            
        "1. A short description\n"
        "2. List of ingredients\n"
        "3. 5-7 simple steps\n"
        "Format as JSON with keys: 'title', 'ingredients', 'steps'"""
    )












