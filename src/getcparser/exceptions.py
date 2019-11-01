class GetCException(Exception):
    pass


class SynamicGetCParsingError(GetCException):
    """Raised when there is an error in lexing or parsing param string of getc()"""
