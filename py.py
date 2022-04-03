import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s |   > %(message)s"
)

import socket, uuid, threading, os, tqdm, time, sokit, json

import sokit, index_mangar

os.system("cls")
logging.info("Start of program")

PORT = 80

soket = sokit.soket()
index = index_mangar.indexing()
# index.log()
