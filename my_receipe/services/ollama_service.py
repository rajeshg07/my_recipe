
import ollama
import json
from typing import List, Optional
from pydantic import BaseModel
from prompts.prompt_generator import generate_prompt
from schemas.recipe_schema import RecipeResponse, RecipeInput
from schemas.recipe_schema import IngredientItem, RecipeInput

ingredients = [
        IngredientItem(name="chicken"),
        IngredientItem(name="onion"),
        IngredientItem(name="chilli"),
        IngredientItem(name="capsicum"),
        IngredientItem(name="tomato")
    ]

user_input = RecipeInput(
        name="Chicken Curry",
        ingredients=ingredients,
        category="non-veg",
    )



class Ingredient(BaseModel):
    name: str

class RecipeResponse(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]



class RecipeGenerator:
    def __init__(
        self,
        # recipe_name: str,
        # ingredients: List[Ingredient],
        # category: str = "veg/non-veg",
        model_name: str = "deepseek-r1:1.5b",
        temperature: float = 0.7,
        # prompt: Optional[str] = None
    ):
        # self.recipe_name = recipe_name
        # self.ingredients = ingredients
        # self.category = category
        self.model_name = model_name
        self.temperature = temperature
        self.prompt = generate_prompt()

    def generate(self) -> RecipeResponse:
        print(f"Generating recipe using model: {self.model_name}")

        response = ollama.generate(
            model=self.model_name,
            # message = [
            #     {"role": "system", "content":self.prompt},
            #     {"role":"user", "content":user_input}
            # ],
            prompt=self.prompt,
            format=RecipeResponse.model_json_schema(),
            options={"temperature": self.temperature},

        )
        return response["response"]['content']

    #     if format == "json":
    #         try:
    #             data = json.loads(response['response'])
    #             return RecipeResponse(**data)
            
    #         except Exception as e:
    #             print(f"Error parsing JSON: {e}")
    #             # Fallback to text response
    #             return self._create_fallback_response(response['response'])

    #     return self._create_fallback_response(response['response'])

    # def _create_fallback_response(self, recipe_text: str) -> RecipeResponse:
    #     return RecipeResponse(
    #         title=self.recipe_name,
    #         ingredients=[i.name for i in self.ingredients],
    #         steps=[recipe_text]
    #     )

























