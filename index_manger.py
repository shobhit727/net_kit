import logging, os, json, configparser

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s |   > %(message)s")

logger = logging.getLogger("index_manger")
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s |   > %(message)s")
logger.setLevel(logging.DEBUG)


class set_up:
    def __init__(self) -> None:
        logger.info("Starting up ")

        self.index = {}

        if os.path.exists(r"data/index.json"):
            logger.debug("index file exists")
            with open(r"data/index.json", "r") as f:
                self.index = json.load(f)
        else:
            logger.info("index file dose not exists")
            index_file = open("data/index.json", "x")
            self.index = {}
