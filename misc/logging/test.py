# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import logging

logformat = '%(asctime)s - %(name)-12s %(levelname)-8s %(message)s'
logging.basicConfig(format=logformat, filename='logfile.log', filemode='w', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')

logging.info("Test info")
logging.debug("Test debug")


a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
    logging.exception("Exception occurred")
