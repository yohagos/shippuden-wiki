import logging
from fastapi import FastAPI
from routes.router import configureRouter
from database.db import engine

from models.characters import Base as characters_base
from models.techniques import Base as techniques_base
from models.villages import Base as villages_base
from models.image_files import Base as image_files_base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app = configureRouter(app)

try:
    characters_base.metadata.create_all(engine)
    techniques_base.metadata.create_all(engine)
    villages_base.metadata.create_all(engine)
    image_files_base.metadata.create_all(engine)
except Exception as e:
    logger.error("Error creating tables: %s", e)
