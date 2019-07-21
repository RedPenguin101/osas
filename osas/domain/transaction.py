# transaction.py

class Transaction:
    def __init__(self):
        self.entries = []

    def set_description(self, description: str):
        self.description = description
