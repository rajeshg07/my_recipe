# Importing tools to work with JSON, logging errors, and the Ollama AI model
import json
import logging
import ollama

# Setting up logging to save errors or info to a file called "recipe_generator.log"
logging.basicConfig(level=logging.INFO, filename="recipe_generator.log",
                   format="%(asctime)s - %(levelname)s - %(message)s")

# This class handles talking to the Ollama AI model to generate recipes
class OllamaService:
    def __init__(self, model_name: str):
        self.model_name = model_name                # Store the model name
        if not self._is_model_installed():           # Check if the model is already installed on the computer

            # If the model isn't installed, try to download it
            logging.warning(f"Model '{model_name}' not found. Attempting to pull...")   
            try:
                ollama.pull(model_name)     # Download the model
                logging.info(f"Successfully pulled model '{model_name}'")
            except Exception as e:
                # If downloading fails, use a default model instead
                logging.error(f"Failed to pull model: {str(e)}. Using default 'deepseek-r1:1.5b'")
                self.model_name = "deepseek-r1:1.5b"


# This function checks if the chosen model is installed
    def _is_model_installed(self):
        try:
            # Get a list of all installed models (e.g., ["deepseek", "llama", "qwen"])
            models = [m["name"].split(":")[0] for m in ollama.list()["models"]]

            # Return True if our model is in the list, False otherwise
            return self.model_name in models
        
        except Exception as e:
            # If something goes wrong (e.g., Ollama isn't running), log the error and return False
            logging.error(f"Failed to check models: {str(e)}")
            return False


# This function asks the AI model to generate a recipe for a given dish
    def generate_recipe(self, dish_name: str, stream: bool = True) -> dict:

         # Create a prompt (instructions) for the Model
        # We ask for a recipe with up to 10 steps, returned as a JSON list
        prompt = f"""Give me a recipe for {dish_name}. Limit to 10 steps. 
        Return only cooking instructions, numbered step-by-step, in clear format.
        Respond in JSON with a 'steps' key containing a list of steps."""

        try:
             # If stream is True, show the model's response as it comes in live
            if stream:
                print("Streaming response:\n")
                full_response = ""

                 # Get the response in small chunks from the LLM model
                for chunk in ollama.chat(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    stream=True
                ):
                    content = chunk.get("message", {}).get("content", "") # Extract the text from each chunk
                    print(content, end="", flush=True)
                    full_response += content
                print()
            else:
                 # If stream is False, get the full response at once
                print("Generating response...\n")
                response = ollama.chat(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    stream=False
                )
                # Extract the text from the response
                full_response = response.get("message", {}).get("content", "")


            # The model should return JSON (e.g., {"steps": ["Step 1", "Step 2"]})
            # Find the JSON part of the response (between { and })
            start = full_response.index('{')
            end = full_response.rindex('}') + 1
            json_data = json.loads(full_response[start:end])
            # Get the "steps" from the JSON, or use a default if it's missing
            steps = json_data.get("steps", ["No steps found."])
             # Ensure steps is a list (even if the model returns a single string)
            return {"steps": steps if isinstance(steps, list) else [steps]}
        except Exception as e:
            # If anything goes wrong (e.g., bad JSON or model error), log it and return an error message
            logging.error(f"Error generating recipe: {str(e)}")
            return {"steps": ["Error generating recipe. Please try again."]}