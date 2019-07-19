import uuid
import datetime

from osas.domain import entry as e


def test_entry_initiates():
    uid = uuid.uuid4()
    date = datetime.date(2019, 1, 1)
    currency = 'GBP'
    amount = 100
    debit = True

    ent = e.Entry(uid, date, currency, amount, debit)

    assert ent.id == uid
    assert ent.date == date
    assert ent.amount == 100
    assert ent.currency == 'GBP'
    assert ent.debit


def test_entry_initiates_from_dict():
    uid = uuid.uuid4()
    date = datetime.date(2019, 1, 1)
    currency = 'GBP'
    amount = 100

    ent_dict = {
            "id": uid,
            "date": date,
            "currency": currency,
            "amount": amount,
            "debit": True
            }

    ent = e.Entry.from_dict(ent_dict)

    assert ent.id == uid
    assert ent.date == date
    assert ent.amount == 100
    assert ent.currency == 'GBP'


def test_entry_to_dict():
    uid = uuid.uuid4()
    date = datetime.date(2019, 1, 1)
    currency = 'GBP'
    amount = 100
    debit = True

    ent_dict = {
            "id": uid,
            "date": date,
            "currency": currency,
            "amount": amount,
            "debit": debit,
            }

    ent = e.Entry.from_dict(ent_dict)

    assert ent.to_dict() == ent_dict


def test_is_debit_or_credits():
    uid = uuid.uuid4()
    date = datetime.date(2019, 1, 1)
    currency = 'GBP'
    amount = 100
    debit = True

    ent = e.Entry(uid, date, currency, amount, debit)

    assert ent.is_debit()
    assert not ent.is_credit()
