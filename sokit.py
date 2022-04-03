import logging, socket

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s |   > %(message)s"
)


class soket:
    def __init__(self) -> None:
        logging.info("Start of soket.__init__()")
        self.PORT = 80
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as net:
            net.bind((self.IP_ADDRESS, self.PORT))
            net.listen()
        # self.a = socket.bind((self.IP_ADDRESS, self.PORT))
        logging.info(f"l_ip> {self.IP_ADDRESS}, port> {self.PORT}")
