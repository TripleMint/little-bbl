 #! /usr/bin/env python

import littlebbl
import six
import pytest
from utils.exceptions import *


def test_unicode_returned():
    k = littlebbl.resolve('20', 'east 68th street', '3B', 'MH')
    assert isinstance(k[0], six.text_type)
    assert isinstance(k[1], six.text_type)
    assert isinstance(k[2], six.text_type)


def test_borough_codes():
    assert littlebbl.get_borough_number('MH') == '1'
    assert littlebbl.get_borough_number('BX') == '2'
    assert littlebbl.get_borough_number('BK') == '3'
    assert littlebbl.get_borough_number('QN') == '4'
    assert littlebbl.get_borough_number('SI') == '5'


def test_borough_exception():
    with pytest.raises(InvalidBoroughException):
        littlebbl.resolve('20', 'east 68th street', '3B', 'NO')
