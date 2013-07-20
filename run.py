#!/usr/bin/env python
import os
import re

# get
from urllib2 import urlopen
from urllib import urlretrieve
import lxml.html

from dumptruck import DumpTruck

import parse

def get(url, cachedir = 'downloads'):
    'Download a web file, or load the version from disk.'
    tmp1 = re.sub(r'^https?://', '', url)
    tmp2 = [cachedir] + filter(None, tmp1.split('/'))
    local_file = os.path.join(*tmp2)
    local_dir = os.path.join(*tmp2[:-1])
    del(tmp1)
    del(tmp2)

    # mkdir -p
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # Download
    if not os.path.exists(local_file):
       print 'Downloading and saving %s' % url
       urlretrieve(url, filename = local_file)

    return lxml.html.parse(local_file).getroot()

SKIPPED_DISTRICTS = {
    'http://www.lrp.usace.army.mil',
    'http://www.mvm.usace.army.mil',
    'http://www.lrb.usace.army.mil',
    'http://www.lre.usace.army.mil',
    'http://www.mvr.usace.army.mil',
    'http://www.mvk.usace.army.mil',
    'http://www.aed.usace.army.mil',
    'http://www.lrb.usace.army.mil',
    'http://www.lre.usace.army.mil',
    'http://www.nan.usace.army.mil',
    'http://www.nao.usace.army.mil',
    'http://www.nau.usace.army.mil',
    'http://www.nwk.usace.army.mil',
    'http://www.nwo.usace.army.mil',
    'http://www.nws.usace.army.mil',
    'http://www.nww.usace.army.mil',
    'http://www.pof.usace.army.mil',
    'http://www.poj.usace.army.mil',
    'http://www.saw.usace.army.mil',
    'http://www.spa.usace.army.mil',
    'http://www.spk.usace.army.mil',
    'http://www.spl.usace.army.mil',
    'http://www.swf.usace.army.mil',
    'http://www.swg.usace.army.mil',
    'http://www.tam.usace.army.mil',
}

if __name__ == '__main__':
    dt = DumpTruck(dbname = 'usace.db')
    dt.create_table({'permit_application_number': 'abcd'}, 'notice')
    dt.create_index(['permit_application_number'], 'notice')
    for division in parse.locations(get('http://www.usace.army.mil/Locations.aspx')):
        for district in division['districts']:
            domain = re.sub(r'.usace.army.mil.*$', '.usace.army.mil', district['href'])
            path = '/Missions/Regulatory/PublicNotices.aspx'
            if domain in SKIPPED_DISTRICTS:
                continue

            pn_list = None
            while pn_list == None or pn_list['last_page'] > pn_list['current_page']:
                pn_list =  parse.public_notice_list(get(domain + path))
                dt.upsert(list(pn_list['notices']), 'notice')

