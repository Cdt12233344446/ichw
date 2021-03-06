#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

"""currency.py: A simple yet functional currency exchange calculator.
                In addition to requirements of the assignment, I added:
                1. detailed docstrings and comments
                2. a timer that records running time

__author__ = "Cai Danyang"
__pkuid__  = "1700011774"
__email__  = "1700011774@pku.edu.cn"
"""

from urllib.request import urlopen
from time import clock


def jstr_fetch(currency_from, currency_to, amount_from):
    """fetch the json string from given input
    """
    # append url arguments step-by-step to reduce code length
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php'
    url = url + '?from=' + currency_from
    url = url + '&to=' + currency_to
    url = url + '&amt=' + str(amount_from)

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
    there's no need to handle errors. Therefore, we leave it empty.

    Warning: in real development, this test should be carefully written.
    """
    return False


# The next three tests are merely formal; they should always pass.
def testError():
    """test if errors are handled properly
    """
    assert(True != hasError())


def testfetch():
    """test if docstr is properly read
    """
    rawstr = jstr_fetch('USD', 'USD', 2.5)
    test_jstr = b'{ "from" : "2.5 United States Dollars",'
    test_jstr = test_jstr + b' "to" : "2.5 United States Dollars",'
    test_jstr = test_jstr + b' "success" : true, "error" : "" }'
    assert(test_jstr == rawstr)


def testprocess():
    """Intended to test if rawstr is properly processed.

    However, since jstr_process() is immediately called by exchange(),
    by testing the latter we CAN test the former. So we leave it empty, again.

    Warning: in real development, this test should be carefully written.
    """
    pass


# these are the 'real' tests
def test_A():
    """this test concerns exchange from USD
    """
    assert(1 == exchange('USD', 'USD', 1))                # initial test
    assert(2.0952375 == exchange('USD', 'EUR', 2.5))      # sample test
    assert(272.146438625 == exchange('USD', 'JPY', 2.5))


def test_B():
    """this test concerns exchange to USD
    """
    assert(2.9829553928851 == exchange('EUR', 'USD', 2.5))
    assert(0.38307424745064 == exchange('CNY', 'USD', 2.5))
    assert(0.022965577031166 == exchange('JPY', 'USD', 2.5))


def test_C():
    """this test concerns exchange to and from lesser-known currencies
    """
    assert(4.8955068493151 == exchange('ZMW', 'MXN', 2.5))
    assert(1.9231929528177 == exchange('THB', 'CUP', 2.5))
    assert(0.001958975 == exchange('KPW', 'XDR', 2.5))


def testAll():
    """test all cases"""
    print("Starting basic tests...")
    testError()
    testfetch()
    testprocess()
    print("Basic tests passed.(Time elapsed since execution: "
          + "%.3f" % clock() + " s)" + "\n\nStarting advanced tests...")
    test_A()
    test_B()
    test_C()
    print("Advanced tests passed.(Time elapsed since execution: "
          + "%.3f" % clock() + " s)\n")
    print("All tests passed. Total time elapsed: "
          + "%.3f" % clock() + " s.")


def main():
    print("Choose your option: 1 for running test; 2 for currency exchange.")
    print("Input here: ", end='')
    num = input()
    if num == '1':
        clock()    # start the timer
        print("")  # add a newline for visual neatness
        testAll()
    elif num == '2':
        print("Please specify your parameters:\nCurrency to exchange from:")
        currency_from = input()
        print("Currency to exchange to:")
        currency_to = input()
        print("Amount of currency to exchange from:")
        amount_from = input()
        amount_to = exchange(currency_from, currency_to, amount_from)
        print("Amount of currency to exchange to:\n" + str(amount_to))
    else:
        main()


if __name__ == '__main__':
    main()
