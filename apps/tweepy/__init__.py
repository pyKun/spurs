# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '1.9'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

from apps.tweepy.models import Status, User, DirectMessage, Friendship, SavedSearch, SearchResult, ModelFactory
from apps.tweepy.error import TweepError
from apps.tweepy.api import API
from apps.tweepy.cache import Cache, MemoryCache, FileCache
from apps.tweepy.auth import BasicAuthHandler, OAuthHandler
from apps.tweepy.streaming import Stream, StreamListener
from apps.tweepy.cursor import Cursor

# Global, unauthenticated instance of API
api = API()

def debug(enable=True, level=1):

    import httplib
    httplib.HTTPConnection.debuglevel = level
