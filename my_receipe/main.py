
#from schemas.recipe_schema import IngredientItem, RecipeInput

# from schemas.recipe_schema import IngredientItem, RecipeInput
from services.ollama_service import RecipeGenerator
import json
# def main():
  
    # ingredients = [
    #     IngredientItem(name="chicken"),
    #     IngredientItem(name="onion"),
    #     IngredientItem(name="chilli"),
    #     IngredientItem(name="capsicum"),
    #     IngredientItem(name="tomato")
    # ]

    # user_input = RecipeInput(
    #     name="Chicken Curry",
    #     ingredients=ingredients,
    #     category="non-veg",
    #     model_name="deepseek-r1:1.5b",
    #     temperature=0.7,
    #     format="json",
    #     stream=False,
    #     prompt=" "
    # )

    # service = RecipeGenerator()
    # response = service.generate()

    # print("\n Generated Recipe:\n")
    # print("Title:", response.title)
    # print("Ingredients:", ", ".join(response.ingredients))
    # print("Steps:")
    # for i, step in enumerate(response.steps, start=1):
    #     print(f"  Step {i}: {step}")

if __name__ == "__main__":
    service = RecipeGenerator()
    response = service.generate()

    print(response)
