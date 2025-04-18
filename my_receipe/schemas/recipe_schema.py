from pydantic import BaseModel
from typing import List



class IngredientItem(BaseModel):
    """
    Represents an individual ingredient.
    """
    name: str


# class RecipeInput(BaseModel):
#     """
#     Represents user input for the recipe generation.
#     """
#     name: str
#     ingredients: List[IngredientItem]
#     category: str
#     model_name: str = "deepseek-r1:1.5b"
#     temperature: float = 0.7
#     format: str = "json"
#     stream: bool = False
#     prompt: str = ""

#     ("ingredients")
#     def min_5_ingredients(cls, v):
#         if len(v) < 5:
#             raise ValueError("You need at least 5 ingredients.")
#         return v

#     ("category")
#     def valid_category(cls, v):
#         if v.lower() not in ["veg", "non-veg"]:
#             raise ValueError("Category must be 'veg' or 'non-veg'.")
#         return v.lower()

class RecipeResponse(BaseModel):
    """
    Represents the final recipe response structure.
    """
    name: str
    steps: List[str]

class RecipeInput(BaseModel):
    name:str
    category:str
    ingredients:List[IngredientItem]








