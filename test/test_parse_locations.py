import os
import nose.tools as n
import lxml.html

import parse
import parse._locations as p

html = lxml.html.parse(os.path.join('fixtures', 'parse_locations', 'Locations.aspx')).getroot()
observed = parse.locations(html)

def test_schema():
    'A row should contain the fields `division`, `district` and `subdomain`.'
    n.assert_equal(set(observed[0].keys()), {'text', 'href', 'districts'})
    n.assert_equal(set(observed[0]['districts'][0].keys()), {'text', 'href'})

def test_district_count():
    'The correct number of districts should be returned.'
    n.assert_equal(len(observed), 9)

def test_data():
    n.assert_dict_equal(observed[3], {
       'districts': [ { 'href': u'http://www.nwk.usace.army.mil', 'text': u'Kansas City District'},
                      {'href': u'http://www.nwo.usace.army.mil', 'text': u'Omaha District'},
                      {'href': u'http://www.nwp.usace.army.mil', 'text': u'Portland District'},
                      {'href': u'http://www.nws.usace.army.mil', 'text': u'Seattle District'},
                      {'href': u'http://www.nww.usace.army.mil', 'text': u'Walla Walla District'},
                      {'href': u'http://www.nww.usace.army.mil', 'text': u'Walla Walla District'}
       ],
       'href': u'http://www.nwd.usace.army.mil',
       'text': u'Northwestern Division'
    })

def test_anchor_stripping():
    'Text should be stripped.'
    observed = p._anchor(lxml.html.fromstring('<a href="abc">  \t watermelon  \r  </a>'))
    n.assert_equal(observed['text'], 'watermelon')

@n.nottest
def test_weird_li():
    '"Far East District" should be in there.'
    n.assert_equal(observed[4]['districts'][1], 'Far East District')
