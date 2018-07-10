#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import navigation as nav

addon = xbmcaddon.Addon()
skygo = None


def playLiveTv(manifest_url, package_code, infolabels=None, art=None, parental_rating=0):
    # hardcoded apixId for live content
    apix_id = 'livechannel_127'

    if(not xbmc.getCondVisibility('Window.IsMedia')):
        data = nav.getlistLiveChannelData()
        for tab in data:
            details = nav.getLiveChannelDetails(tab.get('eventList'), manifest_url)
            if details and len(details) == 1:
                for key in details.keys():
                    detail = details.get(key)
                    infolabels, detail['data'] = nav.getInfoLabel(detail.get('type'), detail.get('data'))
                    art = nav.getArt(detail)
                    break

    skygo.play(manifest_url, package_code, parental_rating=parental_rating, info_tag=infolabels, art_tag=art, apix_id=apix_id)