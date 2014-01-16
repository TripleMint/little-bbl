# Tests for little bbl
import littlebbl
import six
# import pytest


def test_unicode_returned():
    k = littlebbl.resolve('310', 'EAST 46TH STREET', '7U', 'MH')
    assert isinstance(k[0], six.text_type)
    assert isinstance(k[1], six.text_type)
    assert isinstance(k[2], six.text_type)


def test_boroughs():
    assert littlebbl.get_borough_number('MH') == '1'
    assert littlebbl.get_borough_number('BX') == '2'
    assert littlebbl.get_borough_number('BK') == '3'
    assert littlebbl.get_borough_number('QN') == '4'
    assert littlebbl.get_borough_number('SI') == '5'
