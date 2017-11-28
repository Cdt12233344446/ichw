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
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php'
    url = url + '?from=' + currency_from
    url = url + '&to=' + currency_to
    url = url + '&amt=' + str(amount_from)

    # open the url and read the return string
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()

    # process the return string to 'extract' the amount
    jstr = docstr.decode('ascii')
    jstr_split = jstr.split(sep=' ')
    index = jstr_split.index('"to"')
    return float(jstr_split[index+2].lstrip('"'))


def hasError():
    """Intended for handling exceptional json strings.

    However, as specified in the Precondition,
    there's no need to handle errors.Therefore we leave it empty.
    """
    return False


def testError():
    """test if errors are handled properly
    """
    assert(False == hasError())


def test_A():
    """one of a series of tests, with this one concerning exchange from USD
    """
    assert(1 == exchange('USD', 'USD', 1))              # initial test
    assert(2.0952375 == exchange('USD', 'EUR', 2.5))
    assert(272.146438625 == exchange('USD', 'JPY', 2.5))


def test_B():
    """one of a series of tests, with this one concerning exchange to USD
    """
    assert(2.9829553928851 == exchange('EUR', 'USD', 2.5))
    assert(0.38307424745064 == exchange('CNY', 'USD', 2.5))
    assert(0.022965577031166 == exchange('JPY', 'USD', 2.5))


def test_C():
    """one of a series of tests, with this one concerning exchange
    to and from less-used currencies
    """
    assert(4.8955068493151 == exchange('ZMW', 'MXN', 2.5))
    assert(1.9231929528177 == exchange('THB', 'CUP', 2.5))
    assert(0.001958975 == exchange('KPW', 'XDR', 2.5))


def testAll():
    """test all cases"""
    testError()
    test_A()
    test_B()
    test_C()
    print("All tests passed")


if __name__ == '__main__':
    testAll()
