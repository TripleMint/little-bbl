# HEADER
# Explain the borough naming
# License
# CREDitsz
# expand the boroguh resolver?

# scrape to identify error type, ie bad addy vs bad unit id
import requests
from bs4 import BeautifulSoup
import six


def get_borough_number(borough_name):
    '''
    return the appropriate borough number, or None
    '''
    return {
        'MH': '1',
        'BX': '2',
        'BK': '3',
        'QN': '4',
        'SI': '5'
        }.get(borough_name, None)


# Your friend.
# Inputs: listing object
# Returns:
#   3-tuple of strings, (borough, block, lot)
#   or returns 0 if failure

def resolve(street_num, street_name, apt_num, borough_name):
    '''
    All parameters should be strings
    '''

    URL = 'http://webapps.nyc.gov:8084/CICS/fin1/find001i'

    # Set the "FAPTNUM" attribute
    # If this building is a condo, then we need to define the
    # apartment number in order to get the correct BBL.

    borough = get_borough_number(borough_name)

    # Generate data to post
    POST_FORM = {
        'FAPTNUM': apt_num,
        'FBORO': borough,
        'FFUNC': 'A',
        'FHOUSENUM': street_num,
        'FSTNAME': street_name
    }

    # Fields should be None. An empty string should not be called
    # an error (eg. an empty string for FAPTNUM is expected for coops)

    # Python 2 and 3 compatible
    values = list(POST_FORM.values()) if six.PY3 else POST_FORM.values()

    if any(x is None for x in values):
        print('Bad Inputs Error: Don\'t have everything needed'
              'to make POST request')
        return 0

    response = requests.post(URL, data=POST_FORM)

    # Try the POST request, and make some soup
    if response.status_code == 200:
        soup = BeautifulSoup(response.text)
    else:
        print('Request Error: Did not get 200 HTTP response code')
        return 0

    lot_tag = soup.find('input', attrs={'name': 'q49_lot'})
    block_tag = soup.find('input', attrs={'name': 'q49_block_id'})

    if lot_tag and block_tag:
        lot = lot_tag.get('value')
        block = block_tag.get('value')

    else:
        error = soup.find(
            'form', attrs={'name': 'FINDMP1A'}).find(
            'font', attrs={'color': 'red'}).text
        if error:
            print("ERROR: {}".format(error))
        else:
            print("Unknown Error")
        return 0

    # Block and lot are already in unicode
    return six.u(borough), block, lot
