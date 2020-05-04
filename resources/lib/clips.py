#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kodi_six.utils import py2_decode
import json
import time
import base64
from Cryptodome.Cipher import AES

try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode


class Clips:

    secret_key = 'XABD-FHIM-GDFZ-OBDA-URDG-TTRI'
    aes_key = ['826cf604accd0e9d61c4aa03b7d7c890', 'da1553b1515bd6f5f48e250a2074d30c']


    def __init__(self, skygo):

        self.skygo = skygo


    def getClipToken(self, content):
        clipType = 'FREE'
        if content == 'ENTITLED USER' or content == 'SUBSCRIBED USER':
            clipType = 'NOTFREE'
        timestamp = str(time.time()).replace('.', '')
        url = 'https://www.skygo.sky.de/SILK/services/public/clipToken?{0}'.format(urlencode({
            'clipType': clipType,
            'version': '12354',
            'platform': 'web',
            'product': 'SG'
        }))
        url = '{0}&_{1}'.format(timestamp)

        r = self.skygo.session.get(url)
        if common.get_dict_value(r.headers, 'content-type').startswith('application/json'):
            return json.loads(py2_decode(r.text[3:len(r.text) - 1]))
        else:
            None


    def buildClipUrl(self, url, token):
        dec = AES.new(self.aes_key[0].decode('hex'), AES.MODE_CBC, iv=self.aes_key[1].decode('hex'))
        path = dec.decrypt(base64.b64decode(token['tokenValue']))
        query = '{0}={1}'.format(token['tokenName'], path)
        return '{0}?{1}'.format(url, query)


    def playClip(self, clip_id):
        if self.skygo.login():
            clip_info = self.skygo.getClipDetails(clip_id)
            token = getClipToken(clip_info['content_subscription'])
            manifest = buildClipUrl(clip_info['videoUrlMSSProtected'], token)

            self.skygo.play(manifest, clip_info['package_code'])
