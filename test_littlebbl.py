# Tests for little bbl
import littlebbl


def test_unicode_returned():
    k = littlebbl.resolve('75', 'West End Ave', 'R9D', 'MH')
    assert isinstance(k[0], unicode)
    assert isinstance(k[1], unicode)
    assert isinstance(k[2], unicode)


def test_boroughs():
    assert littlebbl.get_borough_number('MH') == '1'
    assert littlebbl.get_borough_number('BX') == '2'
    assert littlebbl.get_borough_number('BK') == '3'
    assert littlebbl.get_borough_number('QN') == '4'
    assert littlebbl.get_borough_number('SI') == '5'
