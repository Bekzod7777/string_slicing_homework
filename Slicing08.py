def main(s):
    """
    The s string variable is given. return the characters in the odd position.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s=str(s)
    return s[1:len(s):2]
