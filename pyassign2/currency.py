#!/usr/bin/env python3
"""currency.py: providing functions to implement a simple currency exchange routine using an online currency service.

__author__ = "Liu Yuxin"
__pkuid__  = "1800011832"
__email__  = "1800011832@pku.edu.cn"
"""


def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space"""
    index_of_blank = s.find(' ')
    before_space0 = s[:index_of_blank]
    return before_space0


def test_before_space():
    """To test the before_space function is correct or not."""
    assert before_space('0.8963 Euros') == '0.8963'  


def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote characters"""
    index1 = s.find('"')
    S = s[index1 + 1:]
    index2 = S.find('"') + index1 + 1
    first_inside_quotes0 = s[index1 + 1:index2]
    return first_inside_quotes0


def test_first_inside_quotes():
    """To test the first_inside_quotes function is correct or not."""
    assert first_inside_quotes('A "B C" D "E F" G') == 'B C'


def get_to(json):
    """Returns: The TO value in the response to a currency query."""
    index = json.find('"to"')
    Json = json[index+4:]
    get_to0 = first_inside_quotes(Json)
    return get_to0


def test_get_to():
    """To test the get_to function is correct or not."""
    assert get_to('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }'
                  ) == '2.24075 Euros'


def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query."""
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' \
          + str(amount_from)
    from urllib.request import urlopen
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def test_currency_response():
    """To test the currency_response function is correct or not."""
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
    docstr = doc.read()
    doc.close()
    jstr_standard = docstr.decode('ascii')
    assert jstr_standard == currency_response('USD', 'EUR', 2.5)


def is_currency(currency):
    """Returns: True if currency is a valid currency and False otherwise."""
    json = currency_response(currency, currency, 0)
    index1 = json.find('"success"')
    index2 = index1 + 9
    json = json[index2:]
    if 'true' in json:
        return True
    else:
        return False


def test_is_currency():
    """To test the iscurrency function is correct or not."""
    assert is_currency('AED') is True


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange."""
    if is_currency(currency_from) is True and is_currency(currency_to) is True and type(amount_from) is float:
        json0 = currency_response(currency_from, currency_to, amount_from)
        get_to0 = get_to(json0)
        amount_to = float(before_space(get_to0))
        return amount_to


def test_exchange():
    """To test the exchange function is correct or not."""
    assert str(exchange('AUD','RUB',3.4)) == '166.14714282227'


def testall():
    """test all cases"""
    test_before_space()
    test_first_inside_quotes()
    test_get_to()
    test_currency_response()
    test_is_currency()
    test_exchange()
    print("All tests passed")


def main():
    """main module"""
    testall()


if __name__ == '__main__':
    main()
