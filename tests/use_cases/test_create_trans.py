# testcreatetrans.py
from unittest import mock

from osas.use_cases import create_trans_use_case as uc


def test_create_trans_use_case():
    repo = mock.Mock()
    create_trans = uc.CreateTransactionUseCase(repo)

    assert create_trans.repo == repo

def test_uc_excutes():
    repo = mock.Mock()
    create_trans = uc.CreateTransactionUseCase(repo)

    return_val = create_trans.execute()

    assert type(return_val).__name__ == "Transaction"
