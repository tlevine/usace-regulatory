import os
import nose.tools as n
import lxml.html

import parse._public_notice_list as p

nap1 = lxml.html.parse(os.path.join('fixtures', 'parse_public_notice_list', 'nap-2013-07-19.html')).getroot()
da_list = lxml.html.parse(os.path.join('fixtures', 'parse_public_notice_list', 'nap-2013-07-19-da_list.html')).getroot()
chunk = next(p._chunk_da_list(da_list))

def test_count():
    'The correct number of notices should be returned.'
    observed = p.public_notice_list(nap1)
    pass

def test_chunk_da_list():
    'The da_list should be chunked into five things.'
    observed = p._chunk_da_list(da_list)
    n.assert_equal(len(list(observed)), 5)

def test_permit_application_number():
    n.assert_equal(p._permit_application_number(chunk), '2012-699')
