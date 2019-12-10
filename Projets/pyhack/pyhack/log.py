# -*- coding: utf-8 -*-
# !/usr/bin/env python3


"""
Module logger

Debug (logger.debug): Provide very detailed output. Used for diagnosing
problems.
Info (logger.info): Provides information on successful execution. Confirms if
things are working as expected.
Warning (logger.warn or logger.warning): Issue a warning regarding a problem
that might occur in the future or a recoverable fault.
Error (logger.error): Indicates a problem in the software as it is not
executing as expected.
Critical (logger.critical): Indicates a serious error that might stop the
program from running.

"""


import logging


def setup_custom_logger(name):
    """Création d'un logger.

    On veut logger dans le terminal (ERROR) et dans un fichier de log (DEBUG).

    """
    # create file handler which logs even debug messages
    filehandler = logging.FileHandler(filename="game.log", mode="w", encoding="utf-8")
    filehandler.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    consolehandler = logging.StreamHandler()
    consolehandler.setLevel(logging.WARNING)
    # create formatter and add it to the handlers
    logformat = "%(asctime)s - %(name)-40s %(levelname)-8s %(message)s"
    fileformatter = logging.Formatter(fmt=logformat, datefmt="%d-%b-%y %H:%M:%S")
    consoleformatter = logging.Formatter(fmt="%(levelname)-8s %(message)s")
    filehandler.setFormatter(fileformatter)
    consolehandler.setFormatter(consoleformatter)
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # add the handlers to the logger
    logger.addHandler(filehandler)
    logger.addHandler(consolehandler)

    return logger
