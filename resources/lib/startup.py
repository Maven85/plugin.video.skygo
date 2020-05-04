#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xbmc, xbmcaddon

from .clips import Clips
from .common import Common
from .livetv import LiveTV
from .memcache import Memcache
from .navigation import Navigation
from .skygo import SkyGo
from .vod import VOD
from .watchlist import Watchlist

try:
    from urllib.parse import parse_qsl
except:
    from urlparse import parse_qsl


def run(argv):

    common = Common(xbmcaddon.Addon(), int(argv[1]), Memcache())
    skygo = SkyGo(common)
    nav = Navigation(common, skygo)
    clips = Clips(skygo)
    liveTV = LiveTV(nav, skygo)
    vod = VOD(nav, skygo)
    watchlist = Watchlist(common, nav, skygo)

    params = dict(parse_qsl(argv[2][1:]))

    # Router for all plugin actions
    if 'action' in params:

        xbmc.log('[Sky Go] params = {0}'.format(params))

        if params['action'] == 'playVod':
            vod.playAsset(params['vod_id'], infolabels=common.getDictFromString(params.get('infolabels', None)), art=common.getDictFromString(params.get('art', None)), parental_rating=int(params.get('parental_rating', 0)))
        elif params['action'] == 'playClip':
            clips.playClip(params['id'])
        elif params['action'] == 'playLive':
            liveTV.playLiveTv(asset_id=params.get('vod_id'), manifest_url=params.get('manifest_url'), package_code=params.get('package_code'), infolabels=common.getDictFromString(params.get('infolabels', None)), art=common.getDictFromString(params.get('art', None)), parental_rating=int(params.get('parental_rating', 0)))
        elif params['action'] == 'listLiveTvChannelDirs':
            nav.listLiveTvChannelDirs()
        elif params['action'] == 'listLiveTvChannels':
            channeldir_name = ''
            if 'channeldir_name' in params:
                channeldir_name = params['channeldir_name']
            nav.listLiveTvChannels(channeldir_name)

        elif params['action'] == 'watchlist':
            if 'list' in params:
                page = 0
                if 'page' in params:
                    page = params['page']
                watchlist.listWatchlist(params['list'], page=page)
            else:
                watchlist.rootDir()
        elif params['action'] == 'watchlistAdd':
            watchlist.addToWatchlist(params['id'], params['assetType'])
        elif params['action'] == 'watchlistDel':
            watchlist.deleteFromWatchlist(params['id'])

        elif params['action'] == 'search':
            nav.search()

        elif params['action'] == 'listPage':
            if 'id' in params:
                 nav.listPage(params['id'])
            elif 'path' in params:
                nav.listPath(params['path'])

        elif params['action'] == 'listSeries':
            nav.listSeasonsFromSeries(params['id'], params.get('calltype'))
        elif params['action'] == 'listSeason':
            nav.listEpisodesFromSeason(params['series_id'], params['id'])

        elif params['action'] == 'parentalSettings':
            nav.showParentalSettings()

        elif params['action'] == 'login':
            skygo.setLogin()

        elif params['action'] == 'clearCache':
            nav.clearCache()

        elif params['action'] == 'refresh':
            xbmc.executebuiltin('container.refresh')

    else:
        nav.rootDir()
        common.addon.setSetting('startup', 'false')