Recipe Generator
The Recipe Generator is a simple Python program that lets you get cooking recipes for any dish by using an AI model called **Ollama**. You type in the dish you want **(like "Chicken Fry")**, choose an AI model, and decide if you want the recipe to appear step-by-step or all at once. The program then fetches a recipe with up to 10 steps and displays it neatly.
How It Works
Here’s the step-by-step process of how the program works:

**Start the Program:**

When you run the program, it welcomes you and asks:
Which AI model to use **(e.g., "deepseek").**
What dish you want a recipe for **(e.g., "Chicken Fry").**
Whether you want the recipe to "stream" (show up bit by bit like a live chat) or all at once.


**It checks if the dish name is valid (at least 2 characters long).**


**Set Up the AI:**

The program checks if the AI model you chose is installed on your computer.
If it’s not installed, it tries to download it. If downloading fails, it uses a backup model called "deepseek-r1:1.5b".
This is like making sure the chef is ready to cook.


**Get the Recipe:**

The program sends a request to the AI, asking for a recipe for your dish with up to 10 steps, formatted as a list in JSON (a structured data format).
If you chose "streaming," the recipe appears as the AI writes it.
If you chose "no streaming," the program waits for the full recipe and then shows it.
The AI’s response looks like: {"steps": ["Step 1: Do this", "Step 2: Do that"]}.


**Show the Recipe:**

The program takes the AI’s response, extracts the list of steps, and prints them neatly, like:Recipe Steps:
1. Rinse chicken
2. Marinate with spices
...




**Handle Problems:**

If anything goes wrong (e.g., the AI isn’t working or the dish name is too short), the program:
Shows a friendly error message, like "Error generating recipe. Please try again."
Saves details of the problem to a file called recipe_generator.log for troubleshooting.



**Files in the Project**
The program is split into three Python files:

**recipe_schema.py:**

Defines the "rules" for what the input (dish name) and output (recipe steps) should look like.
Ensures the dish name is at least 2 characters and the recipe steps are a list of instructions.
Think of this as the template for the recipe card.


**ollama_service.py:**

Handles talking to the Ollama AI model to get the recipe.
Checks if the AI model is installed, downloads it if needed, and processes the AI’s response.
This is like the kitchen where the chef (AI) prepares the recipe.


**main.py:**

Runs the program, asks for user input, and shows the final recipe.
It’s like the waiter who takes your order and brings you the food.



**Tools Used**
The program uses the following tools to work:

Python 3.12: The programming language used to write the program.
Pydantic: A Python library that helps define and validate the structure of data (like ensuring the dish name is valid and the recipe steps are a list).
Ollama: An AI tool that runs language models (like "deepseek") to generate recipes. It’s the "chef" that creates the recipe.
JSON: A format used to structure the AI’s response (e.g., {"steps": [...]}).
Python Logging: A built-in Python tool that saves error messages and info to a file (recipe_generator.log) for troubleshooting.

How to Run the Program

**Install Requirements:**

Make sure you have Python 3.12 installed.
Install the required Python libraries by running:pip install pydantic ollama


Install Ollama on your computer (follow instructions at Ollama’s website).
Download an AI model, like deepseek-r1:1.5b, by running:ollama pull deepseek-r1:1.5b




**Run the Program:**

Save the three Python files (recipe_schema.py, ollama_service.py, main.py) in a folder.
Open a terminal, navigate to the folder, and run:python main.py


Follow the prompts to enter the model name, dish name, and streaming preference.


**Example Interaction:**


**Without Streaming**
Welcome to the Recipe Generator!
Enter model name (e.g., deepseek): deepseek-r1:1.5b
What dish would you like a recipe for? Chicken Curry
Streaming output? (yes/no): no
Generating response...


Recipe Steps:
1. Season chicken breast thoroughly with salt and pepper.
2. Mix together garlic, onion, cumin, coriander, red chili flakes, and paprika in a bowl.
3. Heat oil over medium-high heat and add chicken until browned on both sides.
4. Stir in ghee or sesame oil for cooking.
5. Season with the chile mix from step 2.
6. Pour enough water to cover all ingredients, bring to a boil.
7. Reduce heat to low, simmer for 10-12 minutes.
8. Add tomatoes and vegetables (e.g., carrots, celery, green beans) to the pot. Stir well to combine.
9. Remove from heat, serve hot or add spices before serving.
10. Serve immediately.



**With Streaming**
Welcome to the Recipe Generator!
Enter model name (e.g., deepseek): deepseek-r1:1.5b
What dish would you like a recipe for? Chicken Curry
Streaming output? (yes/no): yes
Streaming response:

```json

// {
//   "steps": [
//     {
//       "step": "Cook chicken breast in water until cooked through.",
//       "description": "In a large pot or oven-safe skillet, heat 2 tablespoons of vegetable oil over medium-high heat. Cook chicken breast (about 1/4 pound) until fully cooked and browned on both sides."
//     },
//     {
//       "step": "Boil and soak rice noodles in boiling water for at least 30 minutes.",
//       "description": "Prepare a large pot or pan with enough water to cover the cooked rice noodles. Bring to a boil, then simmer for 30 minutes until tender-crisp."
//     },
//     {
//       "step": "Season chicken and noodles with spices.",
//       "description": "Drain cooked rice noodles, let them drain on paper towels under running water for at least 15 minutes to allow them to soak. Season both chicken breast and noodles with salt, pepper, garlic powder, cumin, paprika."
//     },
//     {
//       "step": "Make curry sauce.",
//       "description": "In a small bowl, combine vegetable oil, broth (or stock), 1 teaspoon garlic powder, 2 tablespoons ginger, 3 fennel seeds, 1 teaspoon paprika, and salt and pepper to taste. Simmer until thickened."
//     },
//     {
//       "step": "Combine chicken, noodles, and curry sauce.",
//       "description": "Put cooked chicken breast into a baking dish or directly into the pan. Place soaked rice noodles in the bottom of a large pot, cover with layers of chicken and noodles, then add the prepared curry sauce for coating."
//     },
//     {
//       "step": "Let sauce simmer and coat chicken.",
//       "description": "Cover the pan with foil to prevent steam from escaping. Let mixture cook until well coated on all sides; about 5-7 minutes."
//     }
//   ]
// }
// ```



