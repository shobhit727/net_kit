import logging, socket
import logging_manger

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s |   > %(message)s")

logger = logging.getLogger("sokit")
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s |   > %(message)s")
logger.setLevel(logging.DEBUG)


socket.socket()
