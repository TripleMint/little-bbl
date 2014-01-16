'''
url: https://suitey.github.io/little-bbl

The MIT License (MIT)

Copyright (c) 2014 Suitey

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# For making HTTP requests
import requests

# For inspecting the response DOM
from bs4 import BeautifulSoup

# For supporting python 2 and 3
import six


def get_borough_number(borough_name):
    '''
    return the appropriate borough number or None
    '''
    return {
        'MH': '1',
        'BX': '2',
        'BK': '3',
        'QN': '4',
        'SI': '5'
        }.get(borough_name, None)


def resolve(street_num, street_name, apt_num, borough_name):
    '''
    All parameters should be strings
    Returns:
        3-tuple of strings, (borough, block, lot)
        Returns None if failure
    '''

    URL = 'http://webapps.nyc.gov:8084/CICS/fin1/find001i'

    # Set the "FAPTNUM" attribute
    # If this building is a condo, then we need to define the
    # apartment number in order to get the correct BBL.

    borough = get_borough_number(borough_name)

    # Break if borough not in MH, BX, BK, QN, SI
    if not borough:
        print 'Invalid Borough... breaking.'
        return

    # Generate data to post
    POST_FORM = {
        'FAPTNUM': apt_num,
        'FBORO': borough,
        'FFUNC': 'A',
        'FHOUSENUM': street_num,
        'FSTNAME': street_name
    }

    # Python 2 and 3 compatible
    values = list(POST_FORM.values()) if six.PY3 else POST_FORM.values()

    if any(x is None for x in values):
        print('Bad Inputs Error: Don\'t have everything needed'
              'to make POST request')
        return None

    # Get the page
    response = requests.post(URL, data=POST_FORM)

    # Make sure got solid response
    if response.status_code == 200:

        # Make some soup
        soup = BeautifulSoup(response.text)
    else:
        print('Request Error: Did not get 200 HTTP response code')
        return None

    # Find lot and block in soup
    lot_tag = soup.find('input', attrs={'name': 'q49_lot'})
    block_tag = soup.find('input', attrs={'name': 'q49_block_id'})

    # Make sure we found block and lot
    if lot_tag and block_tag:
        lot = lot_tag.get('value')
        block = block_tag.get('value')

    else:

        # If we did not get a lot and block we find what the error was
        # in the soup instead
        error = soup.find(
            'form', attrs={'name': 'FINDMP1A'}).find(
            'font', attrs={'color': 'red'}).text
        if error:
            print('ERROR: {}'.format(error))
        else:
            print('Unknown Error')
        return None

    # Block and lot are already in unicode
    return six.u(borough), block, lot
