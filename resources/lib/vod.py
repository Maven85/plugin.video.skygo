#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xbmcgui


class VOD:


    def __init__(self, nav, skygo):

        self.nav = nav
        self.skygo = skygo


    def playAsset(self, asset_id, infolabels=None, art=None, parental_rating=0):
        # get asset details and build infotag from it
        asset_info = self.nav.getAssetDetailsFromCache(asset_id)
        if len(asset_info) > 0:
            manifest_url = asset_info['media_url']
            if 'ms_media_url' in asset_info:
                manifest_url = asset_info['ms_media_url']

            if infolabels is None:
                infolabels, asset_info = self.nav.getInfoLabel(asset_info.get('type', ''), asset_info)

            self.skygo.play(manifest_url, package_code=asset_info['package_code'], parental_rating=parental_rating,
                            info_tag=infolabels, art_tag=art, apix_id=str(asset_info['event_id']), webvod_url=asset_info.get('webvod_canonical_url'))
        else:
            xbmcgui.Dialog().notification('Sky Go: Datenabruf', 'Es konnten keine Daten geladen werden', xbmcgui.NOTIFICATION_ERROR, 2000, True)