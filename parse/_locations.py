def _anchor(anchor):
    # subdomain = unicode(anchor.xpath('@href')[0]).split('.')[1]
    return {
        'href': unicode(anchor.xpath('@href')[0]),
        'text': unicode(anchor.text_content())
    }

def locations(html):
    divisions = html.xpath('//div[@class="ICG_ETH_Title"]/a[@target="_blank"]')
    for division in divisions:
        division
