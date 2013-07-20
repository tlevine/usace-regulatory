#!/usr/bin/env python
import os
import re

# get
from urllib2 import urlopen
from urllib import urlretrieve
import lxml.html

import requests

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

    return lxml.html.parse(local_file)

SKIPPED_DISTRICTS = {
    'http://www.lrp.usace.army.mil',
    'http://www.mvm.usace.army.mil',
    'http://www.lrb.usace.army.mil',
    'http://www.lre.usace.army.mil',
    'http://www.mvr.usace.army.mil',
}

if __name__ == '__main__':
    for division in parse.locations(get('http://www.usace.army.mil/Locations.aspx')):
        for district in division['districts']:
            domain = re.sub(r'.usace.army.mil.*$', '.usace.army.mil', district['href'])
            path = '/Missions/Regulatory/PublicNotices.aspx'
            if domain in SKIPPED_DISTRICTS:
                continue
            print domain
            print domain + path
            print parse.public_notice_list(get(domain + path))
