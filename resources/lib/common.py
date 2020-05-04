#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kodi_six.utils import py2_decode
from ast import literal_eval
from collections import OrderedDict
import xbmc

try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode


class Common:


    def __init__(self, addon, addon_handle, memcache):

        self.addon = addon
        self.addon_handle = addon_handle
        self.memcache = memcache
        self.addon_id = self.addon.getAddonInfo('id')
        self.addon_path = py2_decode(xbmc.translatePath(self.addon.getAddonInfo('path')))
        self.addon_profile = py2_decode(xbmc.translatePath(self.addon.getAddonInfo('profile')))

        self.base_url = 'plugin://{0}'.format(self.addon_id)
        self.startup = self.addon.getSetting('startup') == 'true'


    def build_url(self, query):
        query.update({'zz': ''})
        query = OrderedDict(query.items())
        return '{0}?{1}'.format(self.base_url, urlencode(query))


    def getDictFromString(self, str):
        return literal_eval(str) if str else None


    def get_dict_value(self, dict, key):
        key = key.lower()
        result = [dict[k] for k in dict if k.lower() == key]
        return result[0] if len(result) > 0 else ''