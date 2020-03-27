import logging
from auxiliary_module import *

# # create logger
# module_logger = logging.getLogger(__name__)
#
# class Auxiliary:
#     def __init__(self):
#         self.logger = logging.getLogger(__name__ + '.' + Auxiliary.__name__)
#         self.logger.info('creating an instance of Auxiliary')
#
#     def do_something(self):
#         self.logger.info('doing something')
#         a = 1 + 1
#         self.logger.info('done doing something')
#
# def some_function():
#     module_logger.info('received a call to "some_function"')

def main():
    # create logger with 'spam_application'
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(filename='spam.log', mode='w')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    logformat = '%(asctime)s - %(name)-40s %(levelname)-8s %(message)s'
    formatter = logging.Formatter(fmt=logformat, datefmt='%d-%b-%y %H:%M:%S')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('creating an instance of auxiliary_module.Auxiliary')
    a = Auxiliary()
    logger.info('created an instance of auxiliary_module.Auxiliary')
    logger.info('calling auxiliary_module.Auxiliary.do_something')
    a.do_something()
    logger.info('finished auxiliary_module.Auxiliary.do_something')
    logger.info('calling auxiliary_module.some_function()')
    some_function()
    logger.info('done with auxiliary_module.some_function()')

if __name__ == '__main__':
    main()
