import pytest
import uuid
import datetime

from osas.domain import transaction as t
from osas.domain import entry as e


@pytest.fixture
def mock_entries():
    e1 = e.Entry(uuid.uuid4(), datetime.date(2017, 7, 11), "GBP", 100, True)
    e2 = e.Entry(uuid.uuid4(), datetime.date(2019, 1, 1), "GBP", 100, False)
    e3 = e.Entry(uuid.uuid4(), datetime.date(2019, 1, 1), "GBP", 100, True)
    e4 = e.Entry(uuid.uuid4(), datetime.date(2019, 1, 1), "GBP", 100, False)

    return [e1, e2, e3, e4]


def test_base_transcation_initiates(mock_entries):
    transaction = t.BaseTransaction()

    assert transaction.entries == []


def test_you_can_add_an_entry(mock_entries):
    transaction = t.BaseTransaction()
    transaction.add_entry(mock_entries[0])

    assert transaction.entries[0] == mock_entries[0]


def test_add_multiple_entries(mock_entries):
    tr = t.BaseTransaction()
    tr.add_entries(mock_entries)

    assert len(tr.entries) == 4


def test_balances(mock_entries):
    tr = t.BaseTransaction()
    tr.add_entries(mock_entries)

    assert tr.is_balanced()

    tr.entries[0].debit = False

    assert not tr.is_balanced()


def test_diff_ccys_caught(mock_entries):
    tr = t.BaseTransaction()
    mock_entries[0].currency = "USD"

    with pytest.raises(t.NonMatchingCurrencyException):
        tr.add_entries(mock_entries)
