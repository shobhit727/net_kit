import logging


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s |   > %(message)s"
)

# loging file
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s |   > %(message)s",
    filename="loging_mangar.log",
    filemode="w",
    datefmt="%Y-%m-%d %H:%M:%S",
)
