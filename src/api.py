API_FILE_PATH = 'src/api.txt'

class Api:
    
    def __init__(self):
        self.parse_api_file()
        return
    
    def parse_api_file(self):
        with open(API_FILE_PATH) as f:
            self.api_key = f.readline().strip()
            self.user_id = f.readline().strip()
        
    