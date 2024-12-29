import logging
import logging.handlers
import os


def getLogger(name: str, logFolder: str, level=logging.DEBUG, doStreamOutput=False) -> logging.Logger:
    """
    :param str name: name of the logger
    :param str logFolder: where to save the log to
    :param int level: The log level to output
    :param bool doStreamOutput: whether or not to also output to the stream
    :return:
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():
        
        if not os.path.exists(logFolder):
            os.makedirs(logFolder)

        fileHandler = logging.FileHandler(os.path.join(logFolder, name + '.log'))
        fileHandler.setLevel(level)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        if doStreamOutput:
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(formatter)
            streamHandler.setLevel(level)
            logger.addHandler(streamHandler)

    return logger


def getActiveLogger(defaultName, **kwargs):
    """
    Get whatever active logger we've got going and work with it

    :return logging.Logger:
    """
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    return loggers[0] if loggers else getLogger(defaultName, **kwargs)
