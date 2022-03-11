import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s | > %(message)s"
)


class indexing:
    def __init__(self) -> None:
        logging.info("Starting indexing.__init__")
        self.index = {}
        self.index_file = "index.json"
        self.load_index()

    def load_index(self):
        pass
