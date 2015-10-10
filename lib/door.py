class Door():

    def __init__(self, prize):
        self.is_open = False
        self.prize = prize

    def open(self):
        self.is_open = not self.is_open
