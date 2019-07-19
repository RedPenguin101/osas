import abc

from osas.domain.entry import Entry


class Transcation(abc.ABC):
    @abc.abstractmethod
    def add_entry(self, entry: Entry):
        pass

    @abc.abstractmethod
    def add_entries(self, entries: list):
        pass

    @abc.abstractmethod
    def is_balanced():
        pass


class BaseTransaction(Transcation):
    def __init__(self):
        self.entries = []

    def add_entry(self, entry: Entry):
        self.entries.append(entry)

    def add_entries(self, entries: list):
        ccy_dict = {}
        for entry in entries:
            ccy_dict[entry.currency] = ccy_dict.get(entry.currency, 0) + 1
            if len(ccy_dict) == 1:
                self.entries.append(entry)
            else:
                raise NonMatchingCurrencyException(
                    "The currencies of the entries you are adding don't match"
                )

    def is_balanced(self):
        d = 0
        c = 0
        for entry in self.entries:
            if entry.is_debit():
                d += entry.amount
            else:
                c += entry.amount

        return d-c == 0


class NonMatchingCurrencyException(Exception):
    pass
