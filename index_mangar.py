import logging, os, json

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s | > %(message)s"
)


class indexing:
    def __init__(self) -> None:
        logging.info("Starting indexing.__init__")
        self.index = {}
        self.config = {}
        self.load_config()
        # self.load_index()
        logging.info("Ending indexing.__init__")

    def load_config(self) -> None:
        logging.info("Starting indexing.load_config()")
        try:
            with open("./config.json", "r+") as f:
                try:
                    self.config = json.load(f)
                except json.JSONDecodeError:
                    logging.error("Error loading config.json > JSONDecodeError")
                    self.config = {}
                    f.write(json.dumps(self.config))

        except FileNotFoundError:
            logging.error("config.json not found")
            with open("./config.json", "x") as f:
                self.config = {}
                f.write(json.dumps(self.config))

        except Exception as e:
            logging.critical(e)

        logging.info("Ending indexing.load_config()")

    def load_index(self) -> None:
        logging.info("Starting indexing.load_index()")
        with open(self.config["index"], "r") as f:
            self.index = json.load(f)
        logging.info("Ending indexing.load_index()")
