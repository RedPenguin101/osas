# create_trans_use_case.py

from osas.domain import transaction as t
from osas.domain import entry as e


class CreateTransactionUseCase:
    def __init__(self):
        self.entries = []

    def add_entry(self):
        self.entries.append(e.Entry(None, None, None, None, None))

    def execute(self):
        return t.Transaction()
