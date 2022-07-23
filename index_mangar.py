import logging, os, json, configparser

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s |   > %(message)s"
)
indixlog = logging.getLogger("index_mangar")
