from database import Database
from console import Console
from player import Player
from round import Round
from display import Display

class Master():
    '''Manages the game, calls necessary classes, and transfers information
    between classes.

    Attributes:
        database (Database): An instance of Database()
        console (Console): An instance of Console()
        round (Round): An instance of Round()
        display (Display): An instance of Display()
        keep_playing (Bool): Whether or not to keep running the game
        current_number (Int): The current number
        new_number (Int): The newly generated number
        guess (String): The player's guess
        player (Player): The Player object
    '''

    def __init__(self):
        '''The class initializer.'''
        self.database = Database()
        self.console = Console()
        self.round = Round()
        self.display = Display()
        self.keep_playing = True
        self.player = None
    
    def start_game(self):
        pass

    def get_inputs(self):
        
        current_number = self.round.get_current_number()

        current_num_message, get_guess_message = self.display.get_guess_display(current_number)
        self.console.write(current_num_message)
        guess = self.console.read(get_guess_message)
        self.player.set_guess(guess)
    
    def do_updates(self):
        
        self.round.set_new_number()
        new_number = self.round. get_new_number()

        points, lose_life = self.round.get_points(self.guess)

        self.player.add_points(points)

        if lose_life:
            self.player.lose_life()
        self.round.set_current_number(new_number)
    
    def do_outputs(self):

        round_end_message, continue_message = self.display.get_round_end_display(self.round.get_new_number(), self.player.get_score(), self.player.get_lives())

        
        
        