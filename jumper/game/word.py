class Word:
    def __init__(self):
        self._words = ['', '', '', '']

        self._selected_word = random(self._words)

        # initialize the class with a attribute named selected_word which contains a randomly
        # selected word

    def check_letter(self, letter):
        # check if letter exists in the selected word
        # if it does, return True, otherwise return False