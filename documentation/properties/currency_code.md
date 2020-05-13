---
layout:		property
title:		"currency_code"
schemas:	[account, agreement, collateral, derivative_cash_flow, derivative, exchange_rate, loan, security]
---

# currency_code

---

The **currency_code** represents the currency of the data object and all the relevant monetary types.

Currencies are represented as 3-letter codes in accordance with [ISO 4217][iso4217] standards.

## agreement
The base currency referred to in an [ISDA CSA][isda_csa]. It is relevant to the [MTA][mta] and [Threshold][th].

---

[acc]: https://github.com/suadelabs/fire/blob/master/documentation/properties/accrued_interest.md
[bal]: https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md
[iso4217]: https://en.wikipedia.org/wiki/ISO_4217
[mta]: https://github.com/suadelabs/fire/blob/master/documentation/properties/minimum_transfer_amount.md
[th]: https://github.com/suadelabs/fire/blob/master/documentation/properties/threshold.md
[isda_csa]: https://www.isda.org/a/mDKDE/5english-law-new-csa-exhibit.pdf
