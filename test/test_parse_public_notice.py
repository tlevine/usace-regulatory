import os
import nose.tools as n
import lxml.html

import parse._public_notice as p

nap1 = lxml.html.parse(os.path.join('fixtures', 'parse_public_notice', '2013-510.aspx')).getroot()
mvn1 = lxml.html.parse(os.path.join('fixtures', 'parse_public_notice', 'mvn-2013-1386-cu.aspx')).getroot()

def test_posted_date_raw():
    n.assert_equal(p._posted_date_raw(nap1), '6/27/2013')
    n.assert_equal(p._posted_date_raw(mvn1), '7/19/2013')

def test_expiration_date_raw():
    n.assert_equal(p._expiration_date_raw(nap1), '7/25/2013')
    n.assert_equal(p._expiration_date_raw(mvn1), '8/11/2013')

def test_attachment_href():
    n.assert_equal(p._attachment_href(nap1), '/Portals/39/docs/regulatory/publicnotices/Public%20Notice%202013-0510-76.pdf')
    n.assert_equal(p._attachment_href(mvn1), '/Portals/56/docs/regulatory/publicnotices/2013_1386_jpnall.pdf')

def test_description():
    observed = p._description(nap1)
    member = '''Philadelphia Hyatt Regency Hotel & Marina - This site is  90 feet south of the entrance to the Hyatt Regency Hotel on North Columbus Boulevard.  Proposed work at this location includes the installation of a 24' x 36' floating dock with four (4) 24 inch steel piles to anchor the dock, an 80' x 5' gangway with handrails and a landing platform off the existing bulkhead supported by four (4) 16 inch steel piles. '''
    n.assert_in(member, observed)

    observed = p._description(mvn1)
    member = '''sed project consists of the excavation and deposition of fill to construct residential lots, including subsurface drainage/sewer, roadways for ingress/egress, detention and retention ponds.  Approxim'''
    n.assert_in(member, observed)

def test_notice_href():
    n.assert_equal(p._notice_href(mvn1), '/Missions/Regulatory/PublicNotices/tabid/9321/Article/16212/mvn-2013-1386-cu.aspx')
