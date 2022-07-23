import logging, socket

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s |   > %(message)s"
)
kitlog = logging.getLogger("sokit")
