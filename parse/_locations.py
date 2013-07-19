from itertools import tee, izip

def _pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def _anchor(anchor):
    # subdomain = unicode(anchor.xpath('@href')[0]).split('.')[1]
    return {
        'href': unicode(anchor.xpath('@href')[0]),
        'text': unicode(anchor.text_content())
    }

def locations(html):
    divisions = _pairwise(html.xpath('id("dnn_ctr9438_ModuleContent")/descendant::div[@class="ICG_ETH_Title" or @class="Normal"]'))
    output = []
    for division in divisions:
        info = _anchor(division[0].xpath('descendant::a[@href][position()=last()]')[0])
        districts = map(_anchor, division[1].cssselect('li > a'))
        if len(districts) > 0:
            info['districts'] = districts
            output.append(info)
        else:
            output[-1]['districts'].append(info)
    return output
