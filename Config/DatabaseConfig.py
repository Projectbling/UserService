from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
import os


from Config.EnvConfiguration import GetSettings

settings = GetSettings()

def init_db(app: FastAPI):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )

def generate_models_list(module_path: str):
    models = []
    for root, dirs, files in os.walk(module_path):
        for file in files:
            if file.endswith("model.py"):
                model_path = os.path.join(root, file).replace(os.sep, ".")[:-3]
                models.append(model_path)
    return models

models_list = generate_models_list("MODULES")
TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": models_list,
            "default_connection": "default",
        }
    },
}