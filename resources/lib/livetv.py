#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin


class LiveTV:


    def __init__(self, nav, skygo):

        self.nav = nav
        self.skygo = skygo


    def playLiveTv(self, asset_id=None, manifest_url=None, package_code=None, infolabels=None, art=None, parental_rating=0):
        # hardcoded apixId for live content
        apix_id = 'livechannel_127'
        if asset_id:
            asset_info = self.nav.getAssetDetailsFromCache(asset_id)
            manifest_url = asset_info.get('ms_media_url') if asset_info.get('ms_media_url') else asset_info.get('media_url')
            package_code = asset_info.get('package_code')

        # if(not xbmc.getCondVisibility('Window.IsMedia')):
        #    data = self.nav.getlistLiveChannelData(showWarning=False)
        #    for tab in data:
        #        details = self.nav.getLiveChannelDetails(tab.get('eventList'), manifest_url)
        #        if details and len(details) == 1:
        #            for key in details.keys():
        #                detail = details.get(key)
        #                infolabels, detail['data'] = self.nav.getInfoLabel(detail.get('type'), detail.get('data'))
        #                art = self.nav.getArt(detail)
        #                break

        self.skygo.play(manifest_url, package_code, parental_rating=parental_rating, info_tag=infolabels, art_tag=art, apix_id=apix_id)
