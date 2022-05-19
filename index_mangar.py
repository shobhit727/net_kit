import logging, os, json, configparser

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s |   > %(message)s"
)
CONFIG = configparser.ConfigParser()


class indexing:
    def __init__(self) -> None:
        logging.info("Starting indexing.__init__")
        self.load_config()
        self.index = {}
        # self.load_index()
        logging.info("Ending indexing.__init__")

    def load_config(self) -> None:
        logging.info("Starting indexing.load_config()")  #       my code in python
        try:
            with open("config.ini"):
                pass
        except:
            logging.info("config.ini not found, creating new one")
            with open("config.ini", "w") as configfile:
                CONFIG.add_section("index")
                CONFIG.set("index", "index_path", f"{os.getcwd()}\\index.json")
                CONFIG.write(configfile)
        CONFIG.read(os.path.join(os.getcwd(), "config.ini"))
        self.config = CONFIG["index"]
        logging.info("Ending indexing.load_config()")

    def load_index(self) -> None:
        pass
        """logging.info("Starting indexing.load_index()")
        with open(self.config["index"], "r") as f:
            self.index = json.load(f)
        logging.info("Ending indexing.load_index()")"""
