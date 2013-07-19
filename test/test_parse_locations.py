import os
import nose.tools as n
import lxml.html

import parse

html = lxml.html.parse(os.path.join('fixtures', 'parse_locations', 'Locations.aspx')).getroot()
observed = parse.locations(html)

def test_schema():
    'A row should contain the fields `division`, `district` and `subdomain`.'
    n.assert_equal(set(observed[0].keys()), {'division', 'district', 'subdomain'})

def test_district_count():
    'The correct number of districts should be returned.'
    n.assert_equal(len(observed), 9)
