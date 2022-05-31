from random import randint

class Round():
    '''Manages the current round. Determines whether the player earns points or
    loses a life. Also determines whether or not the game should end.

    Attributes:
        current_number (Int): The current number in use
        new_number (Int): The new number
    '''

    def __init__(self):
        '''The class initializor.'''
        self._current_number = None
        self._new_number = None
    
    def get_points(self, guess):
        #Set initial values for lose_life and points
        points = 0
        lose_life = False
        
        #Check if player guessed correctly
        if self._new_number > self._current_number:
            if guess.lower() == 'h':
                points += 100
            else:
                lose_life = True
        
        return points, lose_life

    def game_over(self, lives):
        '''Checks whether or not the game is over.
        
        Arguments:
            lives (Int): The number of lives the player has left
        
        Returns:
            Bool
        '''
        #Check how many lives the player has remaining
        if lives > 0:
            return False
        else:
            return True
    
    def get_current_number(self):
        '''Returns the current number.
        
        Returns:
            Int
        '''
        return self._current_number
    
    def get_new_number(self):
        '''Returns the new number.

        Returns:
            Int
        '''
        return self._new_number
    
    def set_current_number(self, value):
        '''Sets the current number.

        Arguments:
            value (Int): The value to set the current number to
        '''
        self._current_number = value
    
    def set_new_number(self):
        '''Sets the new number.'''
        self._new_number = randint(1, 100)