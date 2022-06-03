class Player():
    '''An object containing the player's user name and score.

    Attributes:
        _user_name (String): The player's user name
        _score (Int): The player's current score
        _guess (String): The player's current guess
        _lives (Int): The number of lives the player has left
    '''

    def __init__(self, user_name):
        '''The class initializor.
        
        Arguments:
            user_name (String): The player's user name
        '''
        self._user_name = user_name
        self._score = 0
        self._guess = None
        self._lives = 5

    def get_user_name(self):
        '''Returns the player's user name

        Returns:
            String
        '''
        return self._user_name
    
    def get_score(self):
        '''Returns the player's score.

        Returns:
            Int
        '''
        return self._score
    
    def get_guess(self):
        '''Returns the player's guess.

        Returns:
            String
        '''
        return self._guess
    
    def get_lives(self):
        '''Returns the number of lives the player has left.

        Returns:
            Int
        '''
        return self._lives
    
    def add_points(self, points):
        '''Adds points to the player's score.

        Arguments:
            score (Int): The points to add
        '''
        self._score += points
    
    def set_guess(self, guess):
        '''Sets the player's guess.

        Arguments:
            guess (String): The player's guess
        '''
        self._guess = guess
    
    def lose_life(self):
        '''Reduces the number of lives by 1.'''
        self._lives -= 1