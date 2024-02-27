from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
import os
from Config.EnvConfiguration import GetSettings

settings = GetSettings()

engine = create_async_engine(settings.DATABASE_URL)
async_session = sessionmaker(autocommit=False, autoflush=False, 
                            bind=engine, expire_on_commit=False,class_= AsyncSession)

def init_db(app: FastAPI):
    @app.add_event_handler("startup")
    async def startup_event():
        app.state.db = async_session()

    @app.add_event_handler("shutdown")
    async def shutdown_event():
        await app.state.db.close()

def generate_models_list(module_path: str):
    models = []
    for root, dirs, files in os.walk(module_path):
        for file in files:
            if file.endswith("model.py"):
                model_path = os.path.join(root, file).replace(os.sep, ".")[:-3]
                models.append(model_path)
    return models

models_list = generate_models_list("MODULES")


class DB_Context:

    @staticmethod
    async def get_db():
        session = async_session()
        try:
            yield session
        finally:
            await session.close()
# from tortoise import Tortoise
# from tortoise.contrib.fastapi import register_tortoise
# from fastapi import FastAPI
# import os


# from Config.EnvConfiguration import GetSettings

# settings = GetSettings()

# def init_db(app: FastAPI):
#     register_tortoise(
#         app,
#         config=TORTOISE_ORM,
#         generate_schemas=True,
#         add_exception_handlers=True,
#     )

# def generate_models_list(module_path: str):
#     models = []
#     for root, dirs, files in os.walk(module_path):
#         for file in files:
#             if file.endswith("model.py"):
#                 model_path = os.path.join(root, file).replace(os.sep, ".")[:-3]
#                 models.append(model_path)
#     return models

# models_list = generate_models_list("MODULES")
# TORTOISE_ORM = {
#     "connections": {"default": settings.DATABASE_URL},
#     "apps": {
#         "models": {
#             "models": models_list,
#             "default_connection": "default",
#         }
#     },
# }