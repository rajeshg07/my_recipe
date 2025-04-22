# Importing tools to help define and validate data structures  ##pydantic as validation tool
from pydantic import BaseModel, Field
from typing import List

# This class defines what the user's input should look like
class RecipeInput(BaseModel):
      # The user must provide a dish name (e.g., "Chicken Fry")
    # It must be at least 2 characters long and is required
    dish_name: str = Field(..., min_length=2, description="Name of the dish")


# This class defines what the recipe output will look like
class RecipeResponse(BaseModel):
    # The recipe steps will be a list of instructions (e.g., ["Step 1: Do this", "Step 2: Do that"])
    steps: List[str]  


 # This function prints the recipe steps
    def display(self):
        print("\nRecipe Steps:")
         # Loop through each step in the list and print it
        for step in self.steps:
            print(step)


            