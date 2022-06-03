import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Database():
    '''Communicates with the database to save data or retrieve data.

    Attributes:
        _database (Firestore Client): The database client
    '''

    def __init__(self):
        '''The class initializor.'''
        self._database = None
        self._prepare()

    def get_user(self, name):
        '''Retrieves user data for the given user name.

        Arguments:
            name (String): The user name
        
        Returns:
            Dict or String
        '''
        #Get user collection
        users_reference = self._database.collection(u'users')
        docs = users_reference.stream()
        
        #Create doc_exists variable
        doc_exists = False
        
        #Search for user with matching user name
        for doc in docs:
            #Convert document to a dictionary
            doc_dict = doc.to_dict()

            #Check if the user names match
            if doc_dict['username'] == name:
                return doc_dict
        
        #Notify user if user does not exist
        if not doc_exists:
            return 'User does not exist.'

    def create_user(self, name):
        '''Create a new user document with the given user name.

        Arguments:
            name (String): The user name
        
        Returns:
            String or None
        '''
        #Get users documents
        users_reference = self._database.collection(u'users')
        docs = users_reference.stream()
        
        #Check if user name is already taken
        for doc in docs:
            doc_dict = doc.to_dict()

            if doc_dict['username'] == name:
                return 'User name is taken.'
        
        #Create new user document
        data = {'username' : name, 'high_score' : 0}
        self._database.collection(u'users').document(name).set(data)

    def delete_user(self, name):
        '''Deletes the user document with the given user name.

        Arguments:
            name (String): The user name
        '''
        #Get users documents
        users_reference = self._database.collection(u'users')
        docs = users_reference.stream()
        
        #Find the user document to be deleted
        for doc in docs:
            doc_dict = doc.to_dict()

            if doc_dict['username'] == name:
                self._database.collection(u'users').document(name).delete()

    def save_player_high_score(self, name, score):
        '''Saves the player's high score to the associated user document.

        Arguments:
            name (String): The user name
        '''
        #Get users documents
        users_reference = self._database.collection(u'users')
        docs = users_reference.stream()
        
        #Find user document to save high score to
        for doc in docs:
            doc_dict = doc.to_dict()

            if doc_dict['username'] == name:
                self._database.collection(u'users').document(name).update({'high_score' : score})

    def get_player_high_score(self, name):
        '''Retrieves the current player's high score.

        Arguments:
            name (String): The user name
        
        Returns:
            Int
        '''
        #Get users documents
        users_reference = self._database.collection(u'users')
        docs = users_reference.stream()
        
        #Find user document to retrieve high score from
        for doc in docs:
            doc_dict = doc.to_dict()

            if doc_dict['username'] == name:
                return doc_dict['high_score']

    def get_overall_high_score(self):
        '''Retrieves the user data for the user with the current overall high score.
        
        Returns:
            Dict
        '''
        #Get users documents
        users_reference = self._database.collection(u'users')
        docs = users_reference.stream()

        #Create variables
        high_score_user = None
        high_score = 0
        
        #Search for user with highest high score
        for doc in docs:
            doc_dict = doc.to_dict()

            if doc_dict['high_score'] > high_score:
                high_score_user = doc_dict
                high_score = doc_dict['high_score']
        
        return high_score_user

    def _prepare(self):
        '''Sets the database client.'''
        cred = credentials.Certificate(r'game\credentials\hilo-version2-db-3257202d9186.json')
        default_app = firebase_admin.initialize_app(cred, {'projectID' : 'hilo-version2-db'})

        self._database = firestore.client(default_app)