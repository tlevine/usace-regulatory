import os
import nose.tools as n
import lxml.html

import parse._public_notice_list as p

nap1 = lxml.html.parse(os.path.join('fixtures', 'parse_public_notice_list', 'nap-2013-07-19.html')).getroot()
da_list = lxml.html.parse(os.path.join('fixtures', 'parse_public_notice_list', 'nap-2013-07-19-da_list.html')).getroot()

chunker = p._chunk_da_list(da_list)
chunk0 = next(chunker)
chunk1 = next(chunker)

def test_count():
    'The correct number of notices should be returned.'
    n.assert_equal(len(list(p.public_notice_list(nap1)['notices'])), 5)

def test_current_page():
    n.assert_equal(p._current_page(nap1), 1)
    n.assert_equal(p._current_page(da_list), 4)

def test_last_page():
    n.assert_equal(p._last_page(nap1), 7)
    n.assert_equal(p._last_page(da_list), 7)

def test_chunk_da_list_count():
    'The da_list should be chunked into five things.'
    observed = p._chunk_da_list(da_list)
    n.assert_equal(len(list(observed)), 5)

def test_chunk_da_list_chunksize():
    'Each chunk should have three elements.'
    observed = p._chunk_da_list(da_list)
    for o in observed:
        n.assert_equal(len(list(o)), 3)

def test_permit_application_number():
    n.assert_equal(p._permit_application_number(chunk0), '2012-699')

def test_posted_date_raw():
    n.assert_equal(p._posted_date_raw(chunk1), '1/17/2013')

def test_expiration_date_raw():
    n.assert_equal(p._expiration_date_raw(chunk1), '2/1/2013')

def test_description():
    n.assert_equal(p._description(chunk0), 'Approximately 0.75 nautical miles east of the Indian River Inlet, near Rehoboth Beach, Sussex County, Delaware.')

def test_notice_href():
    n.assert_equal(p._notice_href(chunk1), '/Missions/Regulatory/PublicNotices/tabid/4660/Article/8996/2012-1055.aspx')

def test_attachment_href():
    n.assert_equal(p._attachment_href(chunk0), '/Portals/39/docs/regulatory/publicnotices/Public Notice 2012-0699-39.pdf')
