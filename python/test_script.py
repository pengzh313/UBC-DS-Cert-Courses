from script import clean_currency


def test_clean_currency():
    assert type(clean_currency('$120,000')) == str, "output type not a str"
    assert clean_currency('$120,000') == '120000', "incorrect output"
