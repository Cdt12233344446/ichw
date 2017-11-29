#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

"""currency.py: A simple yet functional currency exchange calculator.

__author__ = "Cai Danyang"
__pkuid__  = "1700011774"
__email__  = "1700011774@pku.edu.cn"
"""

from urllib.request import urlopen


def jstr_fetch(fro, to, amu):
    """fetch the json string from given input
    """
    # append url arguments step-by-step to reduce code length
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php'
    url = url + '?from=' + fro
    url = url + '&to=' + to
    url = url + '&amt=' + str(amu)

    # open the url and read the return string
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    return docstr


def jstr_process(rawstr):
    """process the string to 'extract' the amount
    """
    jstr = rawstr.decode('ascii')
    jstr_split = jstr.split(sep=' ')
    index = jstr_split.index('"to"')
    return float(jstr_split[index+2].lstrip('"'))


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
    docstr = jstr_fetch(currency_from, currency_to, amount_from)
    amount_to = jstr_process(docstr)
    return amount_to


def hasError():
    """Intended for handling exceptional json strings.

    However, as specified in the Precondition,
    there's no need to handle errors. Therefore we leave it empty.
    """
    return False


# The next three tests are rather formal; they always pass.
def testError():
    """test if errors are handled properly
    """
    assert(False == hasError())


def testfetch():
    """test if docstr is properly read
    """
    rawstr = jstr_fetch('USD', 'USD', 2.5)
    test_jstr = b'{ "from" : "2.5 United States Dollars", "to" : "2.5 United States Dollars", "success" : true, "error" : "" }'
    assert(test_jstr == rawstr)


def testprocess():
    """Intended to test if rawstr is properly processed.

    However, since jstr_process() is immediately followed by exchange()
    and thus cannot be isolated, testing jstr_process() is equivalent to
    testing exchange(). So we leave it empty again.
    """
    pass


# these are the 'real' tests
def test_A():
    """one of a series of tests, with this one concerning exchange from USD
    """
    assert(1 == exchange('USD', 'USD', 1))              # initial test
    assert(2.0952375 == exchange('USD', 'EUR', 2.5))    # sample test
    assert(272.146438625 == exchange('USD', 'JPY', 2.5))


def test_B():
    """one of a series of tests, with this one concerning exchange to USD
    """
    assert(2.9829553928851 == exchange('EUR', 'USD', 2.5))
    assert(0.38307424745064 == exchange('CNY', 'USD', 2.5))
    assert(0.022965577031166 == exchange('JPY', 'USD', 2.5))


def test_C():
    """one of a series of tests, with this one concerning exchange
    to and from lesser-known currencies
    """
    assert(4.8955068493151 == exchange('ZMW', 'MXN', 2.5))
    assert(1.9231929528177 == exchange('THB', 'CUP', 2.5))
    assert(0.001958975 == exchange('KPW', 'XDR', 2.5))


def testAll():
    """test all cases"""
    testError()
    testfetch()
    testprocess()
    test_A()
    test_B()
    test_C()
    print("All tests passed")


if __name__ == '__main__':
    testAll()
