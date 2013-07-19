import nose.tools as n
import lxml.html

import parse

nap1 = lxml.html.parse('nap-2013-07-19.html').getroot()


def test_count():
    'The correct number of notices should be returned.'
    observed = parse.parse(html)
    n.assert_equal(len(observed['notices']), 5)
