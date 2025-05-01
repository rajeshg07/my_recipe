# import gradio as gr
# from services.ollama_service import OllamaService
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO, filename="recipe_generator.log",
#                     format="%(asctime)s - %(levelname)s - %(message)s")

# # Initialize OllamaService with a model (e.g., 'deepseek-r1:1.5b')
# ollama_service = OllamaService(model_name="deepseek-r1:1.5b")

# def generate_recipe_ui(dish_name, stream):
#     """
#     Function to generate a recipe and format the output for Gradio.
#     """
#     if not dish_name.strip():
#         return "Please enter a dish name."
    
#     try:
#         # Call the OllamaService to generate the recipe
#         recipe = ollama_service.generate_recipe(dish_name, stream=stream)
#         steps = recipe.get("steps", ["No steps found."])
        
#         # Format the steps as a numbered list
#         formatted_steps = "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps))
#         return formatted_steps if formatted_steps else "No recipe generated."
    
#     except Exception as e:
#         logging.error(f"Error in Gradio UI: {str(e)}")
#         return f"Error generating recipe: {str(e)}"

# # Define the Gradio interface
# with gr.Blocks(title="Recipe Generator") as demo:
#     gr.Markdown("# Recipe Generator")
#     gr.Markdown("Enter a dish name to generate a recipe with up to 10 steps.")
    
#     # Input components
#     dish_input = gr.Textbox(label="Dish Name", placeholder="e.g., Chocolate Cake")
#     stream_checkbox = gr.Checkbox(label="Stream Response", value=True)
    
#     # Output component
#     output = gr.Textbox(label="Recipe Steps", lines=10)
    
#     # Button to trigger recipe generation
#     generate_button = gr.Button("Generate Recipe")
    
#     # Connect the button to the generate_recipe_ui function
#     generate_button.click(
#         fn=generate_recipe_ui,
#         inputs=[dish_input, stream_checkbox],
#         outputs=output
#     )

# # Launch the Gradio app
# if __name__ == "__main__":
#     demo.launch(server_name="0.0.0.0", server_port=7860)

# app.py
# import gradio as gr
# from services.ollama_service import OllamaService
# import logging


# logging.basicConfig(level=logging.INFO, filename="recipe_generator.log",
#                     format="%(asctime)s - %(levelname)s - %(message)s")

# ollama_service = OllamaService(model_name="deepseek-r1:1.5b")

# def stream_ui(dish_name):
#     if not dish_name.strip():
#         yield "Please enter a dish name."
#         return

#     for chunk in ollama_service.generate_recipe(dish_name):
#         yield chunk

# # Gradio Interface
# with gr.Blocks(title="Recipe Generator") as demo:
#     gr.Markdown("## Recipe Generator with Streaming")
#     input_box = gr.Textbox(label="Dish Name")
#     output_box = gr.Textbox(label="Recipe Steps", lines=20)
#     btn = gr.Button("Generate")

#     btn.click(fn=stream_ui, inputs=input_box, outputs=output_box)

# if __name__ == "__main__":
#     demo.launch(server_name="0.0.0.0", server_port=7860)


import gradio as gr
from services.ollama_service import OllamaService
import time

ollama_service = OllamaService(model_name="deepseek-r1:1.5b")

def stream_ui(dish_name):
    recipe = ollama_service.generate_recipe(dish_name, stream=True)
    steps = recipe.get("steps", [])
    
    title = f"Steps to prepare {dish_name.strip().title()}\n\n"
    for i in range(len(steps)):
        content = "\n".join(f"{j+1}. {steps[j]}" for j in range(i + 1))
        yield title + content
        time.sleep(0.3)

with gr.Blocks(title="Recipe Generator") as demo:
    gr.Markdown("# Recipe Generator")
    dish_input = gr.Textbox(label="Dish Name", placeholder="e.g., Chicken Curry")
    output = gr.Textbox(label="Recipe Steps", lines=12)
    generate_button = gr.Button("Generate")

    generate_button.click(fn=stream_ui, inputs=dish_input, outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8001)


