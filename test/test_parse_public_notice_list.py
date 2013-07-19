import os
import nose.tools as n
import lxml.html

import parse

nap1 = lxml.html.parse(os.path.join('fixtures', 'parse_public_notice_list', 'nap-2013-07-19.html')).getroot()

def test_count():
    'The correct number of notices should be returned.'
    observed = parse.public_notice_list(nap1)
    n.assert_equal(len(observed['notices']), 5)
