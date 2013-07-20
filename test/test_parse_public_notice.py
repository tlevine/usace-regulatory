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
    n.assert_equal(p._attachment_href(nap1), '/Portals/39/docs/regulatory/publicnotices/Public Notice 2013-0510-76.pdf')
    n.assert_equal(p._attachment_href(mvn1), '/Portals/56/docs/regulatory/publicnotices/2013_1386_jpnall.pdf')

def test_description():
    observed = p._description(nap1)
    member = '''handrails to connect the landing area to the floating dock.'''
    n.assert_in(member, observed)

    observed = p._description(mvn1)
    member = '''Approximately 10,550 cubic yards of earthen fill will be'''
    n.assert_in(member, observed)

def test_notice_href():
    n.assert_equal(p._notice_href(mvn1), '/Missions/Regulatory/PublicNotices/tabid/9321/Article/16212/mvn-2013-1386-cu.aspx')

def test_no_nbsp():
    n.assert_not_in(u'\xa0', p._description(mvn1))
