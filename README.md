# little bbl

[![Build Status](https://travis-ci.org/Suitey/little-bbl.png?branch=master)](https://travis-ci.org/Suitey/little-bbl)

little bbl is a Python library to query nyc.gov data for borough, block and lot info.
little bbl scrapes the NYC DOF page to resolve the BBL for a given address. The DOF page
has proven to be more reliable than scraping ACRIS directly.

Read all about it at [opensource.suitey.com/little-bbl](http://opensource.suitey.com/little-bbl).

## Requirements
 * [Python](http://www.python.org/) (duh)
   * Tested with Python 2.7.5 and 3.3.3 (but we aren't doing anything crazy so it is probably safe to assume it works on 2.7+)
 * [Requests](http://python-requests.org)
   * Tested with 2.0.0 and 2.2.0
 * [BeautifulSoup==4.3.2](http://www.crummy.com/software/BeautifulSoup/)
 * [six](http://pythonhosted.org/six/) (For supporting python 2 and 3)
   * Tested with 1.5.2

## Usage

    import littlebbl

    # Takes street number, street, unit and borough
    > resolved = littlebbl.resolve('20', 'east 68th street', '3B', 'MH')
    > resolved
      Out: (u'1', u'01382', u'1003')  # (borough, block, lot) 
      
The borough codes are:

    'MH' = Manhattan
    'BX' = Bronx
    'BK' = Brooklyn
    'QN' = Queens
    'SI' = Staten Island

## Reliability (disclaimer)

We would be remiss if we did not mention that the data we are getting this from is ruled by the law of the djungle. It is different for coops, condos and condops. And sometimes you actually need a weird unobvious value for the unit id to get access (sorry for digressing). We do however estimate that this will give you what you are looking for about ~80 % of the time.

For a minor digression on the state of the data we recommend reading [this](http://corenyc.com/blog/2008/10/actionable-data/).

## Help me help you

Questions? Improvements? Issues? Use the [github issues tracker](https://github.com/Suitey/little-bbl/issues).

## License

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
