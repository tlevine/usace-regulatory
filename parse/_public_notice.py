import datetime
import lxml.html
import re

def _posted_date_raw(html):
    return html.xpath('//div[@class="da_body"]/p/em[@class="da_black"]/text()')[0].split(': ')[-1]

def _expiration_date_raw(html):
    return html.xpath('//div[@class="da_body"]/em/text()')[0].split(': ')[-1]

def _description(html):
    return re.sub(r'^[^:]+: ', '', html[1].xpath('text()')[0]).rstrip()

def _notice_href(html):
    return html.xpath('//div[@class="da_body"]/p/strong/a/@href')[0].split('.usace.army.mil')[-1]

def _attachment_href(html):
    return chunk[2].xpath('descendant::a/@href')[0]

