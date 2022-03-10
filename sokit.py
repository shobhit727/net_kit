import logging, socket

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s | > %(message)s"
)


class soket:
    def __init__(self) -> None:
        logging.debug("Start of soket.__init__()")
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        self.PORT = 80
