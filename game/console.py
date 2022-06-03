class Console():
    '''Reads user input from the terminal and displays text to the
    terminal.
    '''

    def read(self, prompt):
        '''Takes input from the user.
        
        Arguments:
            prompt (String): A message to be displayed.

        Returns:
            String
        '''

        #Get user response
        response = input(prompt)

        return response
    
    def write(self, message):
        '''Displays text to the terminal.

        Arguments:
            message (String): The message to be displayed.
        '''

        print(message)