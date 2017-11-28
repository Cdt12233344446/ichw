#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

"""currency.py: A simple yet functional currency exchange calculator.

__author__ = "Cai Danyang"
__pkuid__  = "1700011774"
__email__  = "1700011774@pku.edu.cn"
"""

from urllib.request import urlopen

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    # append arguments step-by-step to reduce code length
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?'
    url = url + 'from=' + currency_from
    url = url + '&to=' + currency_to
    url = url + '&amt=' + str(amount_from)
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    print(jstr)

exchange('USD', 'EUR', 2.5)
