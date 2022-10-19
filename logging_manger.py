import logging
import sokit, index_manger

"""
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s |   > %(message)s"
)

# logging file
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s |   > %(message)s",
    filename="logging_manger.log",
    filemode="w",
    datefmt="%Y-%m-%d %H:%M:%S",
)
"""

server_log = logging.getLogger("sokit")
index_manger_log = logging.getLogger("index_manger")


def set_up():
    pass
    # server_log.addFilter()
