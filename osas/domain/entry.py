# entry.py


class Entry:
    def __init__(self, id, date, currency, amount, debit):
        self.id = id
        self.date = date
        self.currency = currency
        self.amount = amount
        self.debit = debit

    @classmethod
    def from_dict(cls, adict: dict):
        return cls(
            id=adict["id"],
            date=adict["date"],
            currency=adict["currency"],
            amount=adict["amount"],
            debit=adict["debit"]
            )

    def to_dict(self):
        return {
                "id": self.id,
                "date": self.date,
                "currency": self.currency,
                "amount": self.amount,
                "debit": self.debit
                }

    def is_debit(self):
        return self.debit

    def is_credit(self):
        return not self.debit
