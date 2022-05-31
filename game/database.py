import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Database():
    '''Communicates with the database to save data or retrieve data.

    Attributes:
        database (Firestore Client): The database client
    '''

    def __init__(self):
        '''The class initializor.'''
        self.database = None
        self._prepare()

    def get_user_name(self, name, code):
        users_reference = self.database.collection(u'users')
        docs = users_reference.stream()
        
        #INCOMPLETE
    
    def create_user(self, name, code):
        pass

    def delete_user(self, name, code):
        pass

    def save_player_high_score(self, score):
        pass

    def get_high_score(self):
        pass

    def _prepare(self):
        cred = credentials.Certificate('credentials\hilo-version2-db-3257202d9186.json')
        default_app = firebase_admin.initialize_app(cred, {'projectID' : 'hilo-version2-db'})

        self.database = firestore.client(default_app)
