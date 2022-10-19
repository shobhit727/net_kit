import logging, socket
import logging_manger

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s |   > %(message)s",
)

logger = logging.getLogger("sokit")
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s |   > %(message)s")
logger.setLevel(logging.DEBUG)


#       to be completed
