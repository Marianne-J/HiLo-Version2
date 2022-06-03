from game.database import Database
from game.console import Console
from game.player import Player
from game.round import Round
from game.display import Display
from random import randint

class Master():
    '''Manages the game, calls necessary classes, and transfers information
    between classes.

    Attributes:
        _database (Database): An instance of Database()
        _console (Console): An instance of Console()
        _round (Round): An instance of Round()
        _display (Display): An instance of Display()
        _keep_playing (Bool): Whether or not to keep running the game
        _player (Player): The Player object
    '''

    def __init__(self):
        '''The class initializer.'''
        self._database = Database()
        self._console = Console()
        self._round = Round()
        self._display = Display()
        self._keep_playing = True
        self._player = None
    
    def start_game(self):
        '''Prepares and starts the game.'''
        #Prepare the game
        self._prepare()

        #Start the game
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        '''Gets the player's guess and saves it to the Player object.'''
        #Get current number
        current_number = self._round.get_current_number()

        #Get user's guess
        while True:
            current_num_message, get_guess_message = self._display.get_guess_display(current_number)
            self._console.write(current_num_message)
            guess = self._console.read(get_guess_message)

            #Check to make sure guess is valid
            if guess.lower() != 'h' and guess.lower() != 'l':
                self._console.write('\nInvalid response.')
            else:
                break
        
        #Save user's guess to Player object
        self._player.set_guess(guess)
    
    def _do_updates(self):
        '''Updates the state of the game.'''
        #Generate a new number
        self._round.set_new_number()
        new_number = self._round.get_new_number()

        #Determine whether player earns points or loses a life
        points, lose_life = self._round.get_points(self._player.get_guess())

        #Save the amount of points earned to the Player object
        self._player.add_points(points)

        #Check if player has lost a life and subtract a life if True
        if lose_life:
            self._player.lose_life()
        
        #Set the new number as the current number
        self._round.set_current_number(new_number)
    
    def _do_outputs(self):
        '''Displays the results of the round. Mananges the end of game display when
        the game is over.
        '''
        #Get messages
        round_end_message, continue_message = self._display.get_round_end_display(self._round.get_new_number(), self._player.get_score(), self._player.get_lives())

        #Display the round results
        self._console.write(round_end_message)
        
        #Determine if the game is over or not
        self._keep_playing = not self._round.game_over(self._player.get_lives())

        #Check if game is over
        if self._keep_playing:
            #Ask player if they wish to continue playing
            continue_game = self._console.read(continue_message)
            
            #Check if player wishes to continue playing
            if continue_game.lower() == 'y':
                return
            else:
                #Get the player's high score
                high_score_player = self._database.get_player_high_score(self._player.get_user_name())
                
                #If the high score for this game is higher than the player's current high score,
                #set the game's high score as the player's new high score
                if self._player.get_score() > high_score_player:
                    self._database.save_player_high_score(self._player.get_user_name(), self._player.get_score())
                
                #Get the overall high score and the user who achieved that high score, as well as the player's
                #updated high score (assuming it changed)
                high_score_overall = self._database.get_overall_high_score()
                high_score_player = self._database.get_player_high_score(self._player.get_user_name())
                
                #Get the end of game display
                game_over_display = self._display.get_game_over_display(high_score_overall, high_score_player)

                #Display results
                self._console.write(game_over_display)

                #End the game
                self._keep_playing = False
        
        else:
            #Get the player's high score
            high_score_player = self._database.get_player_high_score(self._player.get_user_name())
            
            #If the high score for this game is higher than the player's current high score,
            #set the game's high score as the player's new high score
            if self._player.get_score() > high_score_player:
                self._database.save_player_high_score(self._player.get_user_name(), self._player.get_score())
            
            #Get the overall high score and the user who achieved that high score, as well as the player's
            #updated high score (assuming it changed)
            high_score_overall = self._database.get_overall_high_score()
            high_score_player = self._database.get_player_high_score(self._player.get_user_name())
            
            #Get the end of game display
            game_over_display = self._display.get_game_over_display(high_score_overall, high_score_player)

            #Display results
            self._console.write(game_over_display)

    def _prepare(self):
        '''Allows user to create, delete, and select a user profile and start the game. Also
        sets the initial current number value.'''
        #Create choice variable
        choice = ''

        #Get start screen interface
        ui_message, message_select_user, message_deleted_user, message_created_user = self._display.get_initial_interface()
        
        #Continue looping start screen interface until user starts the game
        while choice.lower() != 'p':
            #Get user's choice
            choice = self._console.read(ui_message)

            #Determine the option the user chose
            if choice.lower() == 's':
                #Get the user name
                user_name = self._console.read(message_select_user)

                #Retrieve user data
                user = self._database.get_user(user_name)
                
                #Determine if user exists
                if user == 'User does not exist.':
                    print(f'\n{user}')
                else:
                    #Create Player object
                    self._player = Player(user['username'])
            
            elif choice.lower() == 'd':
                #Delete the currently selected user
                self._database.delete_user(self._player.get_user_name())

                #Reset player variable
                self._player = None
                
                #Notify user
                self._console.write(message_deleted_user)
            
            elif choice.lower() == 'c':
                #Get user name
                new_user = self._console.read(message_select_user)

                #Create user if user name is not already taken
                response = self._database.create_user(new_user)
                
                #Check if user name is taken
                if response == 'User name is taken.':
                    self._console.write(f'\n{response}')
                else:
                    #Notify user
                    self._console.write(message_created_user)
            
            #Ensure player has selected a user profile
            elif choice.lower() == 'p' and self._player is None:
                choice = ''
                self._console.write('\nSelect a user.')
            
            elif choice.lower() == 'q':
                #End program
                self._keep_playing = False
                break
            
            elif choice.lower() != 'p':
                self._console.write('\nChoose a valid option.')
        
        #Get initial value for the current number
        self._round.set_current_number(randint(1, 100))