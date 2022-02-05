class Jumper:
    """Representation of the parachute
    
    Attributes:
        _draw (List): Will contain parts that make up the parachute
    """
    def __init__(self):
        self._draw = []


    def draw_jumper(self, list):
        """
        Creates all the pieces for the parachute and jumper and appends
        them into the self.draw list.

        Args:
            self (Jumper): An instance of jumper.
            list: Creates the list to hold the jumper

        Returns:
            list: the new created list
        """

        first_try  = " ___ "

        second_try = "/___\ "

        third_try  = "\   / "

        fourth_try = " \ / "

        head = "  O "

        chest = " /|\ "

        legs = " / \ "

        self._draw.append(first_try)

        self._draw.append(second_try)

        self._draw.append(third_try)

        self._draw.append(fourth_try)

        self._draw.append(head)

        self._draw.append(chest)

        self._draw.append(legs)

        return self._draw

    def draw_parachute(self):
        # iterate over the list to draw the parachute

        # Args:
        #     self(Jumper): An instance of Jumper.
        #     _draw (list): a list of strings that will be used to draw the parachute
        parachute = ''
        drawn_jumper = self.draw_jumper(self._draw)

        for i in drawn_jumper:
            parachute = parachute + i + '\n'

        return parachute

    def delete_parachute(self):
        # delete the parachute if the guess is wrong
        # Args:
        #     self(Jumper): An instance of Jumper.
        #     _draw (list): a list of strings that will be used to draw the parachute
        self._draw.pop(0)