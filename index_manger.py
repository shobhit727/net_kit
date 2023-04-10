import logging, os, json, configparser

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s |   > %(message)s")

logger = logging.getLogger("index_manger")
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s |   > %(message)s")
logger.setLevel(logging.DEBUG)


class set_up:
    def __init__(self) -> None:
        logger.info("Starting up ")

        self.index = {}

        # seting up data file
        if os.path.exists(r"data/index.json"):
            logger.debug("index file exists")
            with open(r"data/index.json", "r") as f:
                self.index = json.load(f)
        else:
            logger.info("index file dose not exists")
            with open("data/index.json", "x") as index_file:
                index_file.write(str(self.index))

        if os.path.exists(r"config.yml"):
            logger.debug("config file exists")
        else:
            logger.info("config file is creart")
            with open("config.yml", "x") as config_file:
                pass
