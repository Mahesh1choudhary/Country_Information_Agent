import json
import os

from app.commons.service_logger import setup_logger

COUNTRIES_MAP = {}
FIELDS_MAP = {}
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

logger = setup_logger()
def load_data_in_memory():
    global COUNTRIES_MAP, FIELDS_MAP

    logger.info("Loading COUNTRIES_MAP and FIELDS_MAP data in memory")
    country_file_path = os.path.join(CURRENT_DIR, "country_names.json")
    field_file_path = os.path.join(CURRENT_DIR, "field_names.json")
    with open(country_file_path, "r", encoding="utf-8") as f:
        COUNTRIES_MAP = json.load(f)

    with open(field_file_path, "r", encoding="utf-8") as f:
        FIELDS_MAP = json.load(f)
    logger.info("Loaded COUNTRIES_MAP and FIELDS_MAP data in memory")


def unload_data_from_memory():
    logger.info("Unloading COUNTRIES_MAP and FIELDS_MAP data from memory")
    COUNTRIES_MAP.clear()
    FIELDS_MAP.clear()
    logger.info("Unloaded COUNTRIES_MAP and FIELDS_MAP data from memory")