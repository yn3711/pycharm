#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi
import urllib.request
import json

form = '''
<html>
<head>
<title>都道府県</title>
<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>
</head>
<body>
<div style="margin:0 auto; width:500px; background:lavender; padding:10px;">
<h3>都道府県の情報</h3>
<form method="post">
<label>都道府県：</label>
{}
<input type="submit" value="送信" style='background:lightseagreen; color:white;'>
</form>
</div>
</body>
</html>
'''

res = '''
<html>
<head>
<title>Response</title>
<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
</head>
<body>
<div style="margin:0 auto; width:500px; background:peachpuff; padding:10px; border-radius: 20px;">
<p><div style='text-align:center; background:aliceblue;color:white;border-radius:10px;'>{}</div>
<p>{}
</div>
</body>
</html>
'''


def application(environ, start_response):
    url = 'http://www.npocss.com/edu/json/pref.json'
    response = urllib.request.urlopen(url)
    dict = json.loads(response.read().decode('utf8'))
    buf = '<select name="pref">\n'
    op = '<option value="{}">{}</option>\n'
    for pref in dict:
        buf += op.format(pref, pref)
    buf += '</select>\n'
    html = form.format(buf).encode('utf-8')

    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        name = post['pref'].value
        from pygeocoder import Geocoder
        results = Geocoder.geocode(name)
        code = str(results[0].coordinates)
        dat = dict[name]
        name = '<a href="' + dat['url'] + '" target=_blank>' + name + '</a>'
        sbuf = ''
        for key in dat:
            if key == 'name': continue
            sbuf += key + ': ' + dat[key] + '<br>'
            sbuf += 'coordinates: ' + code + '<br>'
        html = res.format(name, sbuf).encode('utf-8')

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]