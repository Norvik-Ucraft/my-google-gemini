import os
import logging

from dotenv import load_dotenv

load_dotenv()

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
logging.basicConfig(
    level=logging.getLevelNamesMapping()[LOGGING_LEVEL],
    format="%(asctime)s:%(name)s:%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
VERTEXAI_JSON_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
