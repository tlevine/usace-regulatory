import datetime
import lxml.html
import re

def _posted_date_raw(html):
    return html.xpath('//div[@class="da_body"]/p/em[@class="da_black"]/text()')[0].split(': ')[-1]

def _expiration_date_raw(html):
    return html.xpath('//div[@class="da_body"]/em/text()')[0].split(': ')[-1]

def _description(html):
    return html.cssselect('div.da_body > div.da_black')[0].text_content().replace(u'\xa0', '')

def _notice_href(html):
    return html.xpath('//div[@class="da_body"]/p/strong/a/@href')[0].split('.usace.army.mil')[-1]

def _attachment_href(html):
    return html.xpath('//span[@class="da_noticerelated_item"][img]/a/@href')[0]

def public_notice(html):
    return {
    #   'permit_application_number': _permit_application_number(html),
        'posted_date': _posted_date_raw(html),
        'expiration_date': _expiration_date_raw(html),
        'notice_href': _notice_href(html),
        'attachment_href': _attachment_href(html),
        'description': _description(html),
    }
