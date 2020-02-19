'''Purpose of this module is to provide logging for all events on the file system.
This module uses the python's built-in logging module so there's no need to install anything extra.
At the moment logs into an unencrypted file called log_file.log by default.

Example of usage:

    from app.logger.logger_engine import addEvent, listEvents

    addEvent('This is the message to be logged') # Adds a log message into the default file
    
    log = listEvents() # Retrieve the default log file and assign it to a variable
    print(log)

    $ 2020-02-14 17:34:51,949 - This is the message to be logged
'''

import logging

# Create a custom loggers
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# Create a handlers
file_handler = logging.FileHandler('app/logger/log_file.log')   # Logs into a file
#console_handler = logging.StreamHandler()                       # Logs into console
file_handler.setLevel(logging.INFO)
# Create a formatter and add it to the handler
file_format = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(file_format)
# Add handler to logger
logger.addHandler(file_handler)

def addEvent(message, dest=None):
    '''Adds an event to the log.

    Parameters:
    -----------
        message:    String containing the log message
        dest:       Filename for the log file as a string
                    Default is log_file.log
                    This parameter is for testing purposes
    '''

    # If dest is provided
    if dest != None:
        # Change the filename
        file_handler = logging.FileHandler(dest)
        file_handler.setLevel(logging.INFO)
        logger.handlers = [file_handler]
        file_handler.setFormatter(file_format)

        # Write message into log file
        logger.info(message)

        # Change the filename back to default
        file_handler = logging.FileHandler('app/logger/log_file.log')
        file_handler.setLevel(logging.INFO)
        logger.handlers = [file_handler]
        file_handler.setFormatter(file_format)
    else:
        logger.info(message)

def listEvents(filename='app/logger/log_file.log'):
    '''Returns the entire log
    
    Parameters
    ----------
        filename:   String containing the filename for the log file to be retrieved
                    Default is log_file.log
                    This parameter is for testing purposes
    '''

    with open(filename, 'r') as f:

        log_file = f.read()

    return log_file