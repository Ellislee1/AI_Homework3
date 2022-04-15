import requests

API_FILE_PATH = 'src/api.txt'
TEAM_ID = '1314'
API_URL = 'https://www.notexponential.com/aip2pgaming/api/index.php'
TEST_GAME_ID = 3451

class Api:
    
    def __init__(self):
        self.parse_api_file()
        self.game_id = TEST_GAME_ID
        # Added dummy user agent because the default python user-agent was being rejected
        self.headers = {'x-api-key': self.api_key, 'userid': self.user_id, 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'XY'}
        return
    
    def parse_api_file(self):
        with open(API_FILE_PATH) as f:
            self.api_key = f.readline().strip()
            self.user_id = f.readline().strip()
    
    def create_game(self, opponent_team_id: str):
        """Create a new game with the specified opponent id."""
        data = {'teamId1': TEAM_ID, 'teamId2': opponent_team_id, 'type': 'game', 'gameType': 'TTT'}
        try:
            response = requests.post(API_URL, headers=self.headers, data=data)
            self.game_id = response.json()['gameId']
        except requests.exceptions.HTTPError as e:
            print('There was an error creating the game: ', e)
        
    def make_move(self, x: int, y: int) -> bool:
        """Make a move at the specified x, y position on the board."""
        move = '' + str(x) + ',' + str(y)
        print('move: ', move)
        data = {'teamId': TEAM_ID, 'type': 'move', 'move': move, 'gameId': self.game_id}
        try:
            response = requests.post(API_URL, headers=self.headers, data=data)
            json = response.json()
            print('status: ', response.status_code)
            print(json)
            if response.status_code == 200:
                return True
            else:
                print('Something went wrong making a move. Status code: ', response.status_code)
        except requests.exceptions.HTTPError as e:
            print('There was an error creating the game: ', e)

        return False
    
    def get_moves(self):
        """Get a list of all the moves from the current game (newest move is at the start)."""
        params = {'type': 'moves', 'gameId': self.game_id, 'count': 20}
        try:
            response = requests.get(API_URL, headers=self.headers, params=params)
            moves = response.json()
            self.moves = moves
            return moves
        except requests.exceptions.HTTPError as e:
            print('There was an error creating the game: ', e)
    