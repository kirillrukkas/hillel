from homework_10 import  get_file_data, log_event, LOG_FILE
import os.path


EXPIRED = "expired"
SUCCESS = "success"
FAILED = "failed"
USER = "VASYA"
USER_1 = "PETYA"
USER_2 = "BOGDAN"

message = "Login event - Username: {}, Status: {}"

class TestLogEvent:

    def setup_method(self, method):
        # pylint: disable=attribute-defined-outside-init
        if os.path.isfile(LOG_FILE):
            os.remove(LOG_FILE)
        self.number_of_log = 0
        

    def teardown_method(self):
        try:
            os.remove(LOG_FILE)
        except OSError as e:       
            print("Error: %s - %s." % (e.filename, e.strerror))

    def test_success(self):
        log_event(USER, SUCCESS)
        self.number_of_log +=1
        assert len(get_file_data(LOG_FILE)) == self.number_of_log, "Unexpected number of notice in log file"
        assert  f"Login event - Username: {USER}, Status: {SUCCESS}" in get_file_data(LOG_FILE)[self.number_of_log-1]  
   

    def test_expired(self):
        log_event(USER, EXPIRED)
        self.number_of_log +=1
        assert len(get_file_data(LOG_FILE)) == self.number_of_log, "Unexpected number of notice in log file"
        assert  f"Login event - Username: {USER}, Status: {EXPIRED}" in get_file_data(LOG_FILE)[self.number_of_log -1]
    
    def test_failed(self):
        log_event(USER, FAILED)
        self.number_of_log +=1
        assert len(get_file_data(LOG_FILE)) == self.number_of_log, "Unexpected number of notice in log file"
        assert  f"Login event - Username: {USER}, Status: {FAILED}" in get_file_data(LOG_FILE)[self.number_of_log-1]
    
    
    def test_one_user_different_status(self):
        for result in [SUCCESS, EXPIRED, FAILED]:
            log_event(USER, result)            
            self.number_of_log +=1
            assert len(get_file_data(LOG_FILE)) == self.number_of_log, "Unexpected number of notice in log file"
            assert  f"Login event - Username: {USER}, Status: {result}" in get_file_data(LOG_FILE)[self.number_of_log-1]

    def test_all_user_with_all_status(self):
        for result in [SUCCESS, EXPIRED, FAILED]:
            for user in [USER, USER_1, USER_2]:
                log_event(user, result)            
                self.number_of_log +=1
                assert len(get_file_data(LOG_FILE)) == self.number_of_log, "Unexpected number of notice in log file"
                assert  f"Login event - Username: {user}, Status: {result}" in get_file_data(LOG_FILE)[self.number_of_log-1]
