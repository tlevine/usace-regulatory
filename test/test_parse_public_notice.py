import os
import nose.tools as n
import lxml.html

import parse._public_notice as p

nap1 = lxml.html.parse(os.path.join('fixtures', 'parse_public_notice', '2013-510.aspx')).getroot()

def test_posted_date_raw():
    '6/27/2013'

def test_expiration_date_raw():
    '7/25/2013'

def test_attachment_href():
    '/Portals/39/docs/regulatory/publicnotices/Public%20Notice%202013-0510-76.pdf'

def test_description():
    observed = p._description(nap1)
    member = 'Philadelphia Hyatt Regency Hotel & Marina - This site is  90 feet south of the entrance to the Hyatt Regency Hotel on North Columbus Boulevard.  Proposed work at this location includes the installation of a 24' x 36' floating dock with four (4) 24 inch steel piles to anchor the dock, an 80' x 5' gangway with handrails and a landing platform off the existing bulkhead supported by four (4) 16 inch steel piles. '
    n.assert_in(member, observed)
