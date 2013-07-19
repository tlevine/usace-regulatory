import datetime
import lxml.html
import re

_WEB_COLUMNS = [
    'permitApplicationNumber',
    'permitApplicationUrl',

    '_description',
    'expirationDate',

    'publicNoticeUrl',
    'drawingsUrl',
]

def public_notice_list(html):
    return {
        'notices': _notices(html),
    }

def _chunk_da_list(html):
    subcontents = html.xpath('//div[@class="da_list"]/br[position()=last()]/following-sibling::*')
    content = []
    for subcontent in subcontents:
        if subcontent.tag == 'hr':
            yield content
            content = []
        elif len(subcontent.xpath('*')) == 0:
            continue
        else:
            content.append(subcontent)

def _permit_application_number(chunk):
    return chunk[0].text_content()

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

def _notices(html):
    da_list = html.xpath('//div[@class="da_list"]')[0]
    for chunk in _chunk_da_list(da_list):
        yield {
            'permit_application_number': _permit_application_number(chunk),
            'posted_date': _posted_date_raw(chunk),
            'expiration_date': _expiration_date_raw(chunk),
            'notice_href': _notice_href(chunk),
            'attachment_href': _attachment_href(chunk),
            'description': _description(chunk),
        }

def _current_page(html):
    return int(html.xpath('//a[@class="dig_pager_button dig_pager_current"]/span/text()')[0])
