# HEADER
# Explain the borough naming
# License
# CREDitsz
# expand the boroguh resolver?

# scrape to identify error type, ie bad addy vs bad unit id
import requests
from BeautifulSoup import BeautifulSoup


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

def get_bbl(street_num, street_name, apt_num, borough_name):
    '''
    '''

    URL = 'http://webapps.nyc.gov:8084/CICS/fin1/find001i'

    # Set the "FAPTNUM" attribute
    # If this building is a condo, then we need to define the
    # apartment number in order to get the correct BBL.

    borough = get_borough_number(borough_name)
    POST_FORM = {
        'FAPTNUM': apt_num,
        'FBORO': borough,
        'FFUNC': 'A',
        'FHOUSENUM': street_num,
        'FSTNAME': street_name
    }

    # Fields should be None. An empty string should not be called
    # an error (eg. an empty string for FAPTNUM is expected for coops)
    if any(x is None for x in POST_FORM.values()):
        print 'ERROR: Missing FORM data for POST request @get_bbl'
        return 0

    page = requests.post(URL, data=POST_FORM)

    # Try the POST request, and make some soup
    if page.status_code == 200:
        soup = BeautifulSoup(page.text)
    else:
        print 'ERROR: bad POST response @get_bbl'
        return 0

    lot_tag = soup.find('input', attrs={'name': 'q49_lot'})
    block_tag = soup.find('input', attrs={'name': 'q49_block_id'})

    if lot_tag and block_tag:
        lot = lot_tag.get('value')
        block = block_tag.get('value')

    else:
        print "Error: HTML parser could not find block or lot @get_bbl"
        return 0

    return borough, block, lot
