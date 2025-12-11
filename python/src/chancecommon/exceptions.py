class InvalidResultError(Exception):
    def __init__(self, invalid_text):
        self.message = f"{invalid_text} is not a valid result."
        super().__init__(self.message)