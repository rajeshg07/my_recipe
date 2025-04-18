
def get_model_config(model_name: str) -> dict:
    supported_models = {
        "deepseek-r1:1.5b": {"temp": 0.7},
        "llama3": {"temp": 0.6},
        "qwen": {"temp": 0.75}
    }
    return supported_models.get(model_name, supported_models["deepseek-r1:1.5b"])
