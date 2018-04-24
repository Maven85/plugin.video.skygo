#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import xbmcaddon
import xbmcgui
import xbmcplugin
import ast

addon = xbmcaddon.Addon()
skygo = None

def playLiveTv(manifest_url, package_code, infolabels='', parental_rating=0):
    #hardcoded apixId for live content
    apix_id = 'livechannel_127'

    info_tag = None
    if infolabels != '':
        info_tag = ast.literal_eval(infolabels)

    skygo.play(manifest_url, package_code, parental_rating=parental_rating, info_tag=info_tag, apix_id=apix_id)
