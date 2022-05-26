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
    '''

    def __init__(self):
        '''The class initializer.'''
        self.database = Database()
        self.console = Console()
        self.round = Round()
        self.display = Display()
        self.keep_playing = True
        self.current_number = None
        self.new_number = None