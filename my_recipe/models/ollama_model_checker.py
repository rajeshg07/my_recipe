

import ollama
import logging


def get_installed_models():
    try:
        model_list = ollama.list().get("models", [])
        return [m.get("model", "").split(":")[0] for m in model_list if "model" in m]
    except Exception as e:
        logging.error(f"Failed to fetch installed models: {str(e)}")
        return []
