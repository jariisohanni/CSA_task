from pathlib import Path
import pytest
from app.logger.logger_engine import addEvent, listEvents

tests_dir = Path(__file__).parent
path_to_log = Path(tests_dir, '..', 'app', 'logger', 'log_test.log')
log_file = path_to_log.resolve()

def test_create_log():
    # Tests that the log file was created
    addEvent('test message', dest='log_test.log')
    
    assert log_file.exists() == True

def test_message_is_correct():
    # Verifies that the message is correct
    # and then removes the file
    
    log = listEvents(filename='log_test.log')
    log_file.unlink()
    
    # split the log into the time stamp and the message
    # and verify that the message in the log file is correct
    log = log.split(' - ')
        
    assert log[1] == 'test message\n'