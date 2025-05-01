
# import ollama
# from services.ollama_service import OllamaService
# from services.ollama_service import generate_recipe

# ollama_service = OllamaService(model_name="deepseek-r1:1.5b")

# def stream_recipe_response(dish_name: str):

#     prompt = f"""Give me a recipe for {dish_name}. Limit to 10 steps. 
#     """

#     try:
       
#         yield f"Generating recipe for {dish_name}...\n\n"

  
#         response_stream = ollama.chat(
#             model=ollama_service.model_name,
#             messages=[{"role": "user", "content": prompt}],
#             stream=True
#         )

#         for chunk in response_stream:
#             content = chunk.get("message", {}).get("content", "")
#             if content:
#                 yield content

#     except Exception as e:
#         yield f"\n\nError occurred: {str(e)}\n"



from services.ollama_service import OllamaService

# ollama_service = OllamaService(model_name="your_model_here")  # replace with your default model

# def stream_recipe_response(dish_name: str, temperature: float = 0.7):
#     chunks = ollama_service.generate_recipe(dish_name, temperature)
    
#     yield f"Generating recipe for {dish_name}...\n\n"
#     for chunk in chunks:
#         content = chunk.get("message", {}).get("content", "")
#         if content:
#             yield content



# def stream_recipe_response(dish_name: str, temperature: float = 0.7):
#     # chunks = OllamaService.generate_recipe(dish_name, temperature)
    
#     yield f"Generating recipe for {dish_name}...\n\n"
    
#     for chunk in chunks:
    
#         if isinstance(chunk, dict):
#             content = chunk.get("message", {}).get("content", "")
#         else:
#             content = chunk  
#         if content:
#             yield content

#     try:
       
#         yield f"Generating recipe for {dish_name}...\n\n"

  
#         response_stream = ollama.chat(
#             model=OllamaService.model_name,
#             messages=[{"role": "user", "content": prompt}],
#             stream=True
#         )

#         for chunk in response_stream:
#             content = chunk.get("message", {}).get("content", "")
#             if content:
#                 yield content

#     except Exception as e:
#         yield f"\n\nError occurred: {str(e)}\n"


import ollama
from services.ollama_service import OllamaService

ollama_service = OllamaService(model_name="Qwen:latest")

def stream_recipe_response(dish_name: str):
     
    system_prompt = (
        "You are an expert chef.\n"
        "Generate recipes that are clear, concise, and easy to follow.\n"
        "Respond only in JSON format with two keys:\n"
        "1. 'title' (string) - the name of the dish.\n"
        "2. 'steps' (list) - numbered list of cooking steps.\n"
        "No extra text, no explanations."
    )
    
    prompt = f"""Give me a recipe for {dish_name}. Limit to 10 steps. 
    Return only cooking instructions, numbered step-by-step, in clear format.
    Respond in JSON with a 'steps' key containing a list of steps."""

    try:
        
        yield f"Generating recipe for {dish_name}...\n"

        # Stream response from Ollama
        response_stream = ollama.chat(
            model=ollama_service.model_name,

            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}

                ],

                # {"role": "user", "content": prompt}],
            stream=True
        )

        # Yield each chunk as it arrives
        for chunk in response_stream:
            content = chunk.get("message", {}).get("content", "")
            if content:
                yield content

    except Exception as e:
        yield f"Error occurred: {str(e)}\n"
