class myModule:
    def __init__(self, number, string):
        self.number = number
        self.string = string
    def __str__(self):
        return (f"Number = {str(self.number)}, String = {self.string}")
