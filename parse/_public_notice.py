import datetime
import lxml.html
import re

def _posted_date_raw(chunk):
    return chunk[1].xpath('text()')[0].split(':')[0]

def _expiration_date_raw(chunk):
    return chunk[1].xpath('em/text()')[0].replace('Expiration date: ', '')

def _description(chunk):
    return re.sub(r'^[^:]+: ', '', chunk[1].xpath('text()')[0]).rstrip()

def _notice_href(chunk):
    return chunk[0].xpath('@href')[0].split('.usace.army.mil')[-1]

def _attachment_href(chunk):
    return chunk[2].xpath('descendant::a/@href')[0]

