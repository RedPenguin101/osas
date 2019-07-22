# testcreatetrans.py
from unittest import mock

from osas.use_cases import create_trans_use_case as uc


def test_create_trans_use_case():
    create_trans = uc.CreateTransactionUseCase()


def test_uc_excutes():
    create_trans = uc.CreateTransactionUseCase()

    return_val = create_trans.execute()

    assert type(return_val).__name__ == "Transaction"


def test_add_entry_to_transaction():
    create_trans = uc.CreateTransactionUseCase()
    create_trans.add_entry()
