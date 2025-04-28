
from fastapi import APIRouter
from schemas.recipe_schema import RecipeInput
from services.ollama_service import OllamaService

router = APIRouter()
ollama_service = OllamaService(model_name="deepseek-r1:1.5b")

@router.post("/recipe")
async def generate_recipe(recipe_input: RecipeInput):
    response = ollama_service.generate_recipe(recipe_input.dish_name, stream=False)
    return response 

# for streaming

