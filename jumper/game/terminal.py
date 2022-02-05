class Terminal:
    """
    Handles terminal operations.
    The responsibility of the Terminal class is to handle the input and output of
    the jumper code.

    Attributes:
        None
    """

    def user_response(self, message):
        """
        Gets the input (text) from the terminal and sends the message to the 
        user.

        Args:
            self (Terminal): An instance of Terminal.
            message (string): The message to display.

        Returns:
            string: The users input as a letter.
        """
        return input(message)

    def output(self, text):
        """
        Outputs the needed Terminal code to print the jumper.

        Args:
            self (Terminal): An instance of Terminal.
            text (variable): A variable that called the jumper draw_parachute()
        """
        pass

    def game_over(self, message):
        """
        Send the game over message from the terminal to the user to read.

        Args:
            self (Terminal): An instance of Terminal.
            message (string): End of game message to let the user know the game is done.
        
        Returns:
            text (string): The text to display.
        """
        print(message)