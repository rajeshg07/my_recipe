# # Importing the classes we need from other files
# from schemas.recipe_schema import RecipeInput, RecipeResponse
# from services.ollama_service import OllamaService

# def main():
#     print("\nWelcome to the Recipe Generator!")
#     # Ask which AI model to use (e.g., "deepseek")
#     model_name = input("Enter model name (e.g., deepseek): ").strip()
#      # Create an OllamaService object to handle talking to the AI model
#     service = OllamaService(model_name)


#     # Ask the user what dish they want a recipe for
#     dish_name = input("What dish would you like a recipe for? ").strip()
#     try:
#          # Validate the dish name (make sure it's at least 2 characters)
#         recipe_input = RecipeInput(dish_name=dish_name)
#     except Exception as e:
#         # If the input is invalid (e.g., too short), show an error and stop
#         print(f"Invalid input: {e}")
#         return


# # Ask if the user wants the response to stream (show text as it arrives) or not
#     stream_mode = input("Streaming output? (yes/no): ").strip().lower() == "yes"
#     # Ask the AI model to generate the recipe
#     response = service.generate_recipe(recipe_input.dish_name, stream_mode)
#     # Create a RecipeResponse object to hold and display the recipe
#     RecipeResponse(**response).display()

# if __name__ == "__main__":
#     main()


# from fastapi import FastAPI
# from my_recipe.routes.recipe_routes import router as recipe_router

# app=FastAPI()


# # app.include_router(recipe_routes.router, prefix="/api")


# app.include_router(recipe_router)

from fastapi import FastAPI
from routes.recipe_routes import router as recipe_router

# app = FastAPI()
app = FastAPI(
    title="Recipe Generator API"
)


app.include_router(recipe_router, prefix="/api", tags=["recipe"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

