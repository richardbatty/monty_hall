class Door():

    def __init__(self, has_prize):
        self.is_open = False
        self.has_prize = has_prize

    def open(self):
        self.is_open = True
