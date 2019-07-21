# create_trans_use_case.py

from osas.domain import transaction as t

class CreateTransactionUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self):
        return t.Transaction()
