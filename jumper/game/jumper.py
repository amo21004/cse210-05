class Jumper:
    """Representation of the parachute
    
    Attributes:
        _draw (List): Will contain parts that make up the parachute
    """

    def __init__(self):
        self._draw = []

        firts_try  = " ___ "

        second_try = "/___\ "

        third_try  = "\   / "

        fourth_try = " \ / "

        head = "  O "

        chest = " /|\ "

        legs = " / \ "

        self._draw.append(firts_try)

        self._draw.append(second_try)

        self._draw.append(third_try)

        self._draw.append(fourth_try)

        self._draw.append(head)

        self._draw.append(chest)

        self._draw.append(legs)

    def draw_parachute(self):
        # iterate over the list to draw the parachute

        # Args:
        #     _draw (list): a list of strings that will be used to draw the parachute
        parachute = ''

        for i in self._draw:
            parachute = parachute + i + '\n'

        return parachute

    def delete_parachute(self):
        # delete the parachute if the guess is wrong
        # Args:
        #     _draw (list): a list of strings that will be used to draw the parachute
        self._draw.pop(0)