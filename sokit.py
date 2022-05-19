import logging, socket

x = logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s |   > %(message)s"
)


class soket:
    def __init__(self) -> None:
        logging.debug("Start of soket.__init__()")
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        logging.info(f"l_ip ")

    def setup(self, port=80) -> None:
        self.PORT = port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as net:
            net.bind((self.IP_ADDRESS, self.PORT))
            net.listen()

    def start(self):
        pass

    def full_setup() -> None:
        pass
