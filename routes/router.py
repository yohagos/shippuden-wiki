from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import character_routes, image_file_routes, technique_routes, village_routes


def configureRouter(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(character_routes.router)
    app.include_router(technique_routes.router)
    app.include_router(village_routes.router)
    app.include_router(image_file_routes.router)
    return app

