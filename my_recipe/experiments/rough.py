
# #to handle ollama models

# import logging 
# def validate_model(self, model_name):
#     installed_models=get_installed_models()
   

#     if model_name in installed_models:
#         logger.info(f"using installed model: {model_name}")
#         return model_name
    
#     else:
#         logger.warning(f" model '{model_name}' not in installed model.try pull default model")
#         try:
#             ollama.pull(model_name)
#             logger.info(f"successfully pulled model '{model_name}'")
#             return model_name
        
#         except Exception as e:
#             logger.modelerror(f"failed to pull the model '{model_name}':{str(e)}.using the default model 'deepseek-r1:1.5b'")
#             return "deepseek-r1:1.5b"


# #to get output in both streaming and as a chunk

# if self.model_name in self.installed_models:
#     logging.info(f"Using installed model: {model_name}")
#     return model_name 
# else:
#     logging.warning(f"Model '{model_name}' not found in installed models. Attempting to pull...")
    
#     try:
#         # Try pulling the requested model
#         ollama.pull(model_name)
#         logging.info(f"Successfully pulled model '{model_name}'")
        
#         # Verify the model is now installed
#         if model_name in self.installed_models:
#             return model_name
#         else:
#             raise Exception(f"Model '{model_name}' not found after pulling")
            
#     except Exception as e:
#         logging.error(f"Failed to pull the model '{model_name}': {str(e)}. Using default model 'deepseek-r1:1.5b'")
        
#         # Verify default model is available
#         if "deepseek-r1:1.5b" in self.installed_models:
#             return "deepseek-r1:1.5b"
#         else:
#             try:
#                 logging.warning("Default model not installed. Attempting to pull default model...")
#                 ollama.pull("deepseek-r1:1.5b")
#                 return "deepseek-r1:1.5b"
#             except Exception as default_e:
#                 logging.critical(f"Failed to pull default model: {str(default_e)}")
#                 raise RuntimeError("No usable model available - could not load either requested or default model")
            

# import ollama
# import json
# import logging
# from prompts.base_prompt import get_prompt

# logger = logging.getLogger(__name__)
# handler = logging.FileHandler("recipe_generator.log")
# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.INFO)

# class OllamaService:                        # This class handles model selection and recipe generation via Ollama
#     def __init__(self, model_name: str):
#         self.model_name = model_name        # Store user-provided model name
#         self.installed_models = self.get_installed_models()  # Get all installed models

#         if self.model_name not in self.installed_models:
#             logger.warning(f"Model '{self.model_name}' not found in installed models. Attempting to pull...")
#             try:
#                 ollama.pull(self.model_name)
#                 logger.info(f"Successfully pulled model '{self.model_name}'")
#             except Exception as e:
#                 logger.error(f"Failed to pull model '{self.model_name}': {str(e)}. Using default model 'deepseek-r1:1.5b'")
#                 self.model_name = "deepseek-r1:1.5b"
#         else:
#             logger.info(f"Using installed model: {self.model_name}")

#     def get_installed_models(self):
#         return [model["name"].split(":")[0] for model in ollama.list()["models"]]

#     def generate_recipe(self, dish_name: str, stream: bool = True) -> dict:
#         prompt = get_prompt(dish_name)

#         if stream:
#             print("Streaming response:\n")
#             full_response = ""
#             try:
#                 for chunk in ollama.chat(
#                     model=self.model_name,
#                     messages=[{"role": "user", "content": prompt}],
#                     stream=True
#                 ):
#                     content = chunk.get("message", {}).get("content", "")
#                     print(content, end="", flush=True)
#                     full_response += content
#                 print()  # newline after stream
#             except Exception as e:
#                 logger.error(f"Error during streaming: {str(e)}")
#                 return {"steps": ["Error generating recipe. Please try again."]}
#         else:
#             print("Generating full response...\n")
#             try:
#                 response = ollama.chat(
#                     model=self.model_name,
#                     messages=[{"role": "user", "content": prompt}],
#                     stream=False
#                 )
#                 full_response = response.get("message", {}).get("content", "")
#                 print(full_response)
#             except Exception as e:
#                 logger.error(f"Error during non-streamed generation: {str(e)}")
#                 return {"steps": ["Error generating recipe. Please try again."]}

#         try:
#             start = full_response.index('{')
#             end = full_response.rindex('}') + 1
#             json_data = json.loads(full_response[start:end])
#             return {"steps": json_data.get("steps", ["No steps found."])}
#         except Exception as e:
#             logger.warning(f"Could not parse JSON: {str(e)}")
#             return {"steps": [full_response]}

# # main.py
# from schemas.recipe_schema import RecipeInput, RecipeResponse
# from services.ollama_service import OllamaService

# def main():
#     print("\n👋 Welcome to the Simple Recipe Generator using Ollama & Deepseek!")
#     model_name = input("Enter the model name you want to use (e.g., deepseek): ")
#     service = OllamaService(model_name=model_name.strip())

#     dish_name = input("What dish would you like a recipe for? ")
#     try:
#         recipe_input = RecipeInput(dish_name=dish_name)
#     except Exception as e:
#         print(f"Invalid input: {e}")
#         return

#     mode = input("Do you want streaming output? (yes/no): ").strip().lower()
#     stream_mode = mode == "yes"

#     response = service.generate_recipe(recipe_input.dish_name, stream=stream_mode)
#     recipe_response = RecipeResponse(**response)
#     recipe_response.display()

# if __name__ == "__main__":
#     main()

# import ollama
# def check_ollama_model():
#     installed_model_list=[]
#     response=ollama.list()["models"]
#     for model in response:
#         installed_model_list.append(model["model"].split(":")[0])
#         return installed_model_list

