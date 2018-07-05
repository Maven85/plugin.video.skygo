#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import navigation as nav

skygo = None


def playAsset(asset_id, infolabels=None, art=None, parental_rating=0):
    # get asset details and build infotag from it
    asset_info = nav.getAssetDetailsFromCache(asset_id)
    manifest_url = asset_info['media_url']
    if 'ms_media_url' in asset_info:
        manifest_url = asset_info['ms_media_url']

    info_tag = None
    if infolabels:
        info_tag = ast.literal_eval(infolabels)
    else:
        info_tag, asset_info = nav.getInfoLabel(asset_info.get('type', ''), asset_info)

    skygo.play(manifest_url, package_code=asset_info['package_code'], parental_rating=parental_rating, info_tag=info_tag, art_tag=art, apix_id=str(asset_info['event_id']))