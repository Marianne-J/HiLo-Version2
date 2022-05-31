class Player():
    '''An object containing the player's user ID and score.

    Attributes:
        user_id (Int): The player's user ID
        score (Int): The player's current score
    '''

    def __init__(self, user_id, score):
        '''The class initializor.
        
        Arguments:
            user_id (Int): The player's user ID
            score (Int): The player's score
        '''
        self._user_id = user_id
        self._score = score

    def get_user_id(self):
        '''Returns the player's user ID

        Returns:
            Int
        '''
        return self._user_id
    
    def get_score(self):
        '''Returns the player's score.

        Returns:
            Int
        '''
        return self._score
    
    def set_score(self, score):
        '''Sets the player's score.

        Arguments:
            score (Int): The current score
        '''
        self._score = score