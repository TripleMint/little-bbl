 #! /usr/bin/env python


class NothingFoundException(Exception):
    '''
    Got a response but the given search parameters did not
    return a BBL
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class CrappyResponseException(Exception):
    '''
    Calleth you... cometh... not I?
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidBoroughException(Exception):
    '''
    They didn't provide a proper borough code
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(
            'The borough code you provided was not one of ' + self.value
        )
