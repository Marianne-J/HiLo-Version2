class Display():
    '''Builds the text to be displayed to the terminal.'''

    def get_initial_interface(self):
        '''Builds the messages for the interface at the start of the
        game.
        
        Returns:
            4 Strings
        '''
        #Create start screen interface
        ui_message = '\n\nSelect User (s)\nDelete Selected User (d)\nCreate User (c)\nPlay (p)\nQuit (q)\n\nSelect an option: '

        #Create messages
        message_select_user = '\nEnter user name: '
        message_deleted_user = '\nUser deleted.'
        message_created_user = "\nUser created. Don't forget to select a user."

        return ui_message, message_select_user, message_deleted_user, message_created_user
    
    def get_guess_display(self, current_num):
        '''Builds and returns the messages for getting the guess.
        
        Arguments:
            current_num (Int): The current number
        
        Returns:
            2 Strings
        '''
        #Create messages
        current_num_message = f'\n\nCurrent number: {current_num}'
        get_guess_message = f'Higher or lower? (h/l): '

        return current_num_message, get_guess_message
    
    def get_round_end_display(self, new_num, score, lives):
        '''Builds and returns the messages displayed at the end of the round.

        Arguments:
            new_num (Int): The new number
            score (Int): The current score
            lives (Int): The number of lives remaining
        
        Returns:
            2 Strings
        '''
        #Create messages
        round_end_message = f'\n\nNew number: {new_num}\nCurrent score: {score}\nLives remaining: {lives}'
        continue_message = 'Continue playing? (y/n): '

        return round_end_message, continue_message
    
    def get_game_over_display(self, overall_high_score, player_high_score):
        '''Builds and returns the messages displayed at the end of the game.
        
        Arguments:
            overall_high_score (Dict): The data for the user with the overall high score
            player_high_score (Int): The current player's high score
        
        Returns:
            String
        '''
        #Set high score and user who achieved that score
        high_score_user = overall_high_score['username']
        high_score = overall_high_score['high_score']

        #Create message
        message = f'\nGame Over!\n\nYour current high score: {player_high_score}\nThe current high score: {high_score} - {high_score_user}\n'

        return message