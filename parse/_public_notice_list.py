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
    print subcontents
    content = []
    for subcontent in subcontents:
        if subcontent.tag == 'hr':
            yield content
        else:
            content.append(subcontent)

def _notices(html):
    da_list = html.xpath('//div[@class="da_list"]')[0]

    table = []
    for rowList in zip(
        da_list.xpath('a[@href]/b/text()'),
        da_list.xpath('a[b]/@href'),

        da_list.xpath('span[@class="da_black"]/text()'),
        da_list.xpath('span[@class="da_black"]/em/text()'),

        da_list.xpath('descendant::div[@class="da_relatedlist_item"]/descendant::a[text()="Public Notice"]/@href'),
        da_list.xpath('descendant::div[@class="da_relatedlist_item"]/descendant::a[text()="Drawings"]/@href'),

    ):
        row = dict(zip(_WEB_COLUMNS, rowList))
        row['expirationDate'] = datetime.datetime.strptime(row['expirationDate'], 'Expiration date: %m/%d/%Y').strftime('%Y-%m-%d')
        row['publicNoticeDate'] = datetime.datetime.strptime(m.group(1), '%m/%d/%Y').strftime('%Y-%m-%d')
        row['projectDescription'] = m.group(2)
        row['parish'] = m.group(3).lower()
        row['applicant'] = m.group(4)

        del(row['_description'])
        table.append(row)
    return table
