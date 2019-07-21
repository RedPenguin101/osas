import pytest
from osas.domain import transaction as t


def test_base_transcation_initiates():
    transaction = t.Transaction()

    assert transaction.entries == []


def test_set_description():
    trans = t.Transaction()
    trans.set_description("test name")

    assert trans.description == "test name"
