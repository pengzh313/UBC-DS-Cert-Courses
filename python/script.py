def clean_currency(dollar_value):
    """
    Remove currency symbol and delimiters from dollar values.

    Parameters
    ----------
    dollar_value : str
        The strings showing dollar value with currency symbol and delimiters.

    Returns
    -------
    str
        The strings without the currency symbol and delimiters.

    Raises
    ------
    TypeError
        If the input argument dollar_value is not of type str
    
    Examples
    --------
    >>> clean_currency('$100,000')
    '100000'
    """
    
    if type(dollar_value) is not str:
        raise TypeError("You are not using a string for the dollar_value input.")
    
    return(dollar_value.replace('$', '').replace(',', ''))


assert type(clean_currency('$120,000')) == str, "output type not a str"
assert clean_currency('$120,000') == '120000', "incorrect output"
