# OSAS
OSAS is an Open Source Accounting System intended to be used by small to medium sized corporations.

It is focused on eliminating manual entry and amendment of accounting, instead relying on other operational software your company uses, such as trading systems, payroll systems, and invoicing systems to drive it's activity, with the data being passed in through customisable modules.

The accounting data of OSAS is stored in simple database schemas, with the intention that a data-literate organisation can easily customise the way it fetches it's accounting data.

## The core accounting model
The core accounting model of OSAS is extremely simple. An entry consists of an amount, a currency, and an entry date. It also has a unique identifier, and all additional details are added separately and connected via this UID.

`
